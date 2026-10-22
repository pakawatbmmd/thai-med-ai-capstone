#!/usr/bin/env python3
"""Run Codex (OpenAI) and Gemini council rounds through their APIs.

The laptop councils used agentic CLIs that could open repo files. Plain API
calls cannot, so this script reads each council's PROMPTS.md and context files
from git refs and inlines them into the prompt. Outputs go to
council_runs/<council>/<agent>_round<N>.md for review before committing.

Usage:
  python3 tools/run_council.py --list-models
  python3 tools/run_council.py --council v7 --round 1 [--agents codex gemini] [--dry-run]

Authentication: preferably as cloud-environment network secrets, which the agent
proxy injects into requests (api.openai.com: "Authorization: Bearer <key>";
generativelanguage.googleapis.com: "x-goog-api-key: <key>"), so the keys never
enter the session. If OPENAI_API_KEY / GEMINI_API_KEY are set instead, they are
sent directly.

Environment:
  OPENAI_MODEL  (default gpt-6.1-sol)        verify with --list-models
  GEMINI_MODEL  (default gemini-4-argon)     verify with --list-models
  OPENAI_REASONING_EFFORT (default high)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

BRANCH = {
    "v4": "origin/claude/physical-ai-med-ed-research",
    "v5": "origin/claude/medical-harness-research",
    "v6": "origin/claude/future-of-care-research",
    "v7": "origin/claude/decision-model-council",
    "v8": "origin/claude/decision-model-council",
}
DIR = {
    "v4": "council_v4",
    "v5": "council_v5_harness",
    "v6": "council_v6_future_of_care",
    "v7": "council_v7_flip_perspective",
    "v8": "council_v8_clinical_flip",
}
# Files each council's Round 1 prompt tells the agent to read, as (ref, path or
# directory). A directory includes every .md file directly inside it.
ROUND1_CONTEXT = {
    "v4": [
        ("v4", "README.md"),
        ("v4", "reports/Thai physical AI and med education.md"),
        ("v4", "research_notes/Thai physical AI and med education/"),
    ],
    "v5": [
        ("v5", "README.md"),
        ("v5", "reports/Medical agent harness.md"),
        ("v5", "research_notes/Medical agent harness/"),
        ("v5", "reports/Thai medical LLM landscape.md"),
    ],
    "v6": [
        ("v6", "README.md"),
        ("v6", "reports/AI care vectors for Thailand.md"),
        ("v6", "research_notes/AI care vectors for Thailand/"),
        ("v6", "reports/Thai medical LLM landscape.md"),
    ],
    "v7": [
        ("v7", "README.md"),
        ("v7", "council_v7_flip_perspective/brief.md"),
        ("v6", "reports/AI care vectors for Thailand.md"),
    ],
    "v8": [
        ("v8", "README.md"),
        ("v8", "council_v8_clinical_flip/brief.md"),
    ],
}
# Round 2 adds all three Round 1 answers on top of the council's main report.
ROUND2_CONTEXT = {
    "v4": [("v4", "reports/Thai physical AI and med education.md")],
    "v5": [("v5", "reports/Medical agent harness.md")],
    "v6": [("v6", "reports/AI care vectors for Thailand.md")],
    "v7": [("v7", "council_v7_flip_perspective/brief.md")],
    "v8": [("v8", "council_v8_clinical_flip/brief.md")],
}

PREAMBLE = """You are running through an API, not an agentic CLI, so you cannot open files.
Every file the instructions below tell you to read is inlined after the instructions,
each wrapped in <file path="..."> tags. Treat that as the complete repository view.
Where the instructions say "Write your answer to <path>", reply with the full
markdown content of that file and nothing else.
"""


def git_show(ref, path):
    return subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout


def list_dir(ref, path):
    out = subprocess.run(["git", "ls-tree", "--name-only", f"{ref}:{path.rstrip('/')}"],
                         capture_output=True, text=True, check=True).stdout
    return [path + name for name in out.split() if name.endswith(".md")]


def gather(entries):
    files = []
    for council, path in entries:
        ref = BRANCH[council]
        paths = list_dir(ref, path) if path.endswith("/") else [path]
        for p in sorted(paths):
            files.append((p, git_show(ref, p)))
    return files


def prompt_blocks(council):
    text = git_show(BRANCH[council], f"{DIR[council]}/PROMPTS.md")
    blocks = re.findall(r"```text\n(.*?)```", text, flags=re.S)
    if len(blocks) < 2:
        sys.exit(f"{council}: expected Round 1 and Round 2 ```text blocks in PROMPTS.md")
    return blocks[0], blocks[1]


def build_prompt(council, rnd, agent, round1_answers):
    r1, r2 = prompt_blocks(council)
    instructions = (r1 if rnd == 1 else r2).replace("<AGENT>", agent)
    if rnd == 1:
        files = gather(ROUND1_CONTEXT[council])
    else:
        files = [(f"{DIR[council]}/{name}_round1.md", body) for name, body in round1_answers.items()]
        files += gather(ROUND2_CONTEXT[council])
    inlined = "\n\n".join(f'<file path="{p}">\n{body}\n</file>' for p, body in files)
    return f"{PREAMBLE}\n{instructions}\n\n{inlined}\n", [p for p, _ in files]


def request(url, headers, body=None, retries=4):
    # Transient 5xx responses from the proxy or upstream are retried with backoff.
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code >= 500 and attempt < retries:
                time.sleep(2 ** attempt * 5)
                continue
            sys.exit(f"HTTP {e.code} from {url}: {e.read().decode()[:2000]}")


def auth_headers(agent):
    # Without an env key, the agent proxy's network secret supplies the header.
    key = os.environ.get(KEY[agent])
    if not key:
        return {}
    return {"Authorization": f"Bearer {key}"} if agent == "codex" else {"x-goog-api-key": key}


def call_openai(prompt):
    # High-effort answers take minutes, longer than the proxy holds a connection
    # open, so submit in background mode and poll for the result.
    headers = {**auth_headers("codex"), "Content-Type": "application/json"}
    data = request(
        "https://api.openai.com/v1/responses",
        headers,
        {
            "model": os.environ.get("OPENAI_MODEL", "gpt-6.1-sol"),
            "reasoning": {"effort": os.environ.get("OPENAI_REASONING_EFFORT", "high")},
            "input": prompt,
            "background": True,
        },
    )
    while data.get("status") in ("queued", "in_progress"):
        time.sleep(15)
        data = request(f"https://api.openai.com/v1/responses/{data['id']}", headers)
    if data.get("status") != "completed":
        sys.exit(f"OpenAI response {data.get('id')} ended {data.get('status')}: {data.get('error') or data.get('incomplete_details')}")
    parts = [c["text"] for item in data.get("output", []) if item.get("type") == "message"
             for c in item.get("content", []) if c.get("type") == "output_text"]
    return "".join(parts)


def call_gemini(prompt, retries=3):
    # Gemini has no background mode, so stream (with thought summaries, which keep
    # bytes flowing while it thinks) to stop the proxy from dropping an idle request.
    model = os.environ.get("GEMINI_MODEL", "gemini-4-argon")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent?alt=sse"
    body = json.dumps({
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"thinkingConfig": {"includeThoughts": True}},
    }).encode()
    headers = {**auth_headers("gemini"), "Content-Type": "application/json"}
    for attempt in range(retries + 1):
        text = []
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=600) as resp:
                for line in resp:
                    line = line.decode().strip()
                    if not line.startswith("data:"):
                        continue
                    chunk = json.loads(line[5:])
                    for cand in chunk.get("candidates", []):
                        for part in cand.get("content", {}).get("parts", []):
                            if not part.get("thought"):
                                text.append(part.get("text", ""))
            return "".join(text)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ConnectionError) as e:
            code = getattr(e, "code", None)
            if (code is None or code >= 500) and attempt < retries:
                time.sleep(2 ** attempt * 5)
                continue
            detail = e.read().decode()[:2000] if hasattr(e, "read") else str(e)
            sys.exit(f"Gemini error ({code}): {detail}")


CALL = {"codex": call_openai, "gemini": call_gemini}
KEY = {"codex": "OPENAI_API_KEY", "gemini": "GEMINI_API_KEY"}


def list_models():
    for agent, url, field, key in (
        ("codex", "https://api.openai.com/v1/models", "data", "id"),
        ("gemini", "https://generativelanguage.googleapis.com/v1beta/models?pageSize=200", "models", "name"),
    ):
        try:
            data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=auth_headers(agent))))
            print(f"{agent}:", sorted(m[key] for m in data[field]))
        except urllib.error.HTTPError as e:
            print(f"{agent}: HTTP {e.code} (is the network secret or {KEY[agent]} set?)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--council", choices=sorted(BRANCH))
    ap.add_argument("--round", type=int, choices=[1, 2])
    ap.add_argument("--agents", nargs="+", default=["codex", "gemini"], choices=sorted(CALL))
    ap.add_argument("--dry-run", action="store_true", help="build prompts and report sizes without calling APIs")
    ap.add_argument("--list-models", action="store_true")
    args = ap.parse_args()

    if args.list_models:
        return list_models()
    if not args.council or not args.round:
        ap.error("--council and --round are required")

    out_dir = os.path.join("council_runs", args.council)
    os.makedirs(out_dir, exist_ok=True)

    round1_answers = {}
    if args.round == 2:
        ref, d = BRANCH[args.council], DIR[args.council]
        for name in ("claude", "codex", "gemini"):
            local = os.path.join(out_dir, f"{name}_round1.md")
            if os.path.exists(local):
                round1_answers[name] = open(local).read()
            else:
                round1_answers[name] = git_show(ref, f"{d}/{name}_round1.md")

    for agent in args.agents:
        prompt, paths = build_prompt(args.council, args.round, agent, round1_answers)
        print(f"[{args.council} r{args.round} {agent}] {len(prompt):,} chars, {len(paths)} files")
        if args.dry_run:
            continue
        text = CALL[agent](prompt)
        path = os.path.join(out_dir, f"{agent}_round{args.round}.md")
        with open(path, "w") as f:
            f.write(text)
        print(f"  wrote {path} ({len(text):,} chars)")


if __name__ == "__main__":
    main()
