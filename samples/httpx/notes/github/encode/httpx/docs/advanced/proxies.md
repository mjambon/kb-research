# Explain proxies

tags: config docs security transport

Explains forwarding and tunneling through HTTP proxies, proxy authentication, SOCKS support, and troubleshooting. `/github/encode/httpx/httpx/_client.py` selects proxy routes using URL patterns from `/github/encode/httpx/httpx/_utils.py`; `/github/encode/httpx/httpx/_transports/default.py` constructs the network proxy transport. Proxy behavior also depends on environment settings described in `/github/encode/httpx/docs/environment_variables.md`. Published via `/github/encode/httpx/mkdocs.yml`.
