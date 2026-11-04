# Adapt HTTPX requests to httpcore network pools

tags: api async error security transport

`HTTPTransport` and `AsyncHTTPTransport` construct httpcore pools or proxy connections using SSL, limits, HTTP versions, and socket options. They convert HTTPX requests and byte streams to httpcore calls, wrap response streams for cleanup, and map httpcore failures through `map_httpcore_exceptions` into `/github/encode/httpx/httpx/_exceptions.py`. `/github/encode/httpx/httpx/_client.py` instantiates these unless a custom transport is supplied. Mapping completeness is tested in `/github/encode/httpx/tests/test_exceptions.py`.
