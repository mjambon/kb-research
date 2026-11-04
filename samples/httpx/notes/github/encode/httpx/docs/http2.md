# Explain http/2

tags: docs transport

Explains enabling HTTP/2 with the optional dependency and `http2=True`, and inspecting the negotiated version on a response. `/github/encode/httpx/httpx/_transports/default.py` passes HTTP version preferences to httpcore; `/github/encode/httpx/pyproject.toml` declares the `http2` extra. Enabling HTTP/2 does not force every server connection to use it. Published via `/github/encode/httpx/mkdocs.yml`.
