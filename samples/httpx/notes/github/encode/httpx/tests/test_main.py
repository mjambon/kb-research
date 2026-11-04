# Verify main behavior

tags: cli testing

Uses the Click runner to exercise `/github/encode/httpx/httpx/_main.py` help, GET and POST, JSON and binary display, redirects, verbose tracing, authentication, downloads, and error output. The CLI is an optional extra declared in `/github/encode/httpx/pyproject.toml`; these tests check command behavior rather than the Python request API alone.
