# Verify proxies behavior

tags: config security testing transport

Exercises client proxy routing and transport selection in `/github/encode/httpx/httpx/_client.py` using URL patterns from `/github/encode/httpx/httpx/_utils.py`. Cases cover SOCKS, explicit mounts, environment proxies, unsupported schemes, and closing sync or async proxy transports. This is the place to check route priority and resource cleanup when changing proxy configuration. Shared fixtures come from `/github/encode/httpx/tests/conftest.py`.
