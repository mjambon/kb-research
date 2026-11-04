# Send async requests directly into an ASGI application

tags: api async transport

`ASGITransport` constructs an ASGI HTTP scope, feeds the request body through `receive`, collects `http.response.start` and body messages, and returns a streamed `Response`. Its event helper supports asyncio and Trio. `raise_app_exceptions` determines whether app failures propagate; lifespan startup is outside this transport. `/github/encode/httpx/tests/test_asgi.py` covers scopes, body transfer, completion, and failures; `/github/encode/httpx/docs/advanced/transports.md` documents use.
