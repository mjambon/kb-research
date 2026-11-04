# Implement the optional command line client

tags: cli api

The Click command parses method, URL, headers, body, JSON, authentication, redirect, TLS, and download options, then uses HTTPX to send and display a request. Rich and Pygments format output; tracing and download helpers handle detailed or streamed output. `/github/encode/httpx/pyproject.toml` declares the `httpx` command and `/github/encode/httpx/httpx/__init__.py` supplies the missing-extra fallback. `/github/encode/httpx/tests/test_main.py` exercises CLI behavior.
