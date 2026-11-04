# Answer requests with a user supplied handler

tags: api async testing transport

`MockTransport` calls a handler returning a `Response` in either sync or async requests. It is useful for deterministic client tests without a network and is selected through the custom transport parameter of `/github/encode/httpx/httpx/_client.py`. The handler owns response content; client send logic still applies auth, redirects, and stream cleanup.
