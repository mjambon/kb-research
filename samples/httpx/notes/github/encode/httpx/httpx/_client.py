# Coordinate synchronous and asynchronous HTTP requests

tags: api async auth request security transport

`BaseClient` merges base URL, headers, query parameters, cookies, timeout, authentication, and event hooks. `Client` and `AsyncClient` share the policy but use distinct transport and stream lifecycles. `build_request` merges client defaults; `send` accepts a prepared request and sets timeout extensions, then drives auth and redirects before invoking the selected transport. `USE_CLIENT_DEFAULT` distinguishes omitted per-request settings from explicit `None`. Per-request `cookies=` still works but emits a deprecation warning because its persistence semantics are ambiguous. Redirect handling checks origins before forwarding credentials; transport mounts and environment proxies route by URL pattern. Bound streams set elapsed time when closed. Follow changes with `/github/encode/httpx/tests/client/` and `/github/encode/httpx/tests/test_timeouts.py`.
