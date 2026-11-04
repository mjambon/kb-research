# Explain resource limits

tags: config docs transport

This guide explains the `limits=` client setting: maximum live connections, maximum idle keepalive connections, and idle expiry. `/github/encode/httpx/httpx/_config.py` defines `Limits`, and `/github/encode/httpx/httpx/_transports/default.py` passes it to httpcore's pool. The documented defaults are 100 total connections, 20 keepalive connections, and five seconds of keepalive expiry. `/github/encode/httpx/mkdocs.yml` publishes the page.
