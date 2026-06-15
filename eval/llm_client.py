"""Minimal client for any OpenAI-compatible chat-completions endpoint.

Configure via environment (e.g. a local .env you export — see .env.example):
  BOOK2SKILL_LLM_BASE_URL   base URL ending in /v1   (required)
  BOOK2SKILL_LLM_MODEL      default model id
  BOOK2SKILL_LLM_API_KEY    api key if the endpoint needs one (default: "not-needed")
  BOOK2SKILL_LLM_PROXY      optional proxy, e.g. socks5h://localhost:1055, for tunneled endpoints
"""
from __future__ import annotations

import os
import re
import requests

BASE_URL = os.getenv("BOOK2SKILL_LLM_BASE_URL", "http://localhost:8000/v1").rstrip("/")
DEFAULT_MODEL = os.getenv("BOOK2SKILL_LLM_MODEL", "")
API_KEY = os.getenv("BOOK2SKILL_LLM_API_KEY", "not-needed")
_PROXY = os.getenv("BOOK2SKILL_LLM_PROXY")
_PROXIES = {"http": _PROXY, "https": _PROXY} if _PROXY else None
_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


class LLMError(RuntimeError):
    """Raised when the endpoint is unreachable or returns an unusable response."""


def chat(messages, *, model=None, temperature=0.0, max_tokens=4000, timeout=240):
    """One chat completion against the configured OpenAI-compatible endpoint.
    Returns (text, usage_dict). Strips a <think>...</think> block from reasoning models.
    """
    payload = {
        "model": model or DEFAULT_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        resp = requests.post(f"{BASE_URL}/chat/completions", json=payload,
                             headers=headers, proxies=_PROXIES, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise LLMError(f"LLM request failed: {exc}") from exc

    data = resp.json()
    try:
        content = data["choices"][0]["message"].get("content") or ""
    except (KeyError, IndexError) as exc:
        raise LLMError(f"unexpected response shape: {data}") from exc

    return _THINK_RE.sub("", content).strip(), data.get("usage", {})


if __name__ == "__main__":
    print(chat([{"role": "user", "content": "Reply with exactly the two characters: OK"}], max_tokens=2000))
