# Explain async support

tags: api async docs

Explains `AsyncClient` requests, async context management, streaming, explicit transports, supported async environments, and calls into Python web apps. `/github/encode/httpx/httpx/_client.py` implements async lifecycle; `/github/encode/httpx/httpx/_transports/asgi.py` handles in-process ASGI calls. The examples require awaiting calls and closing async streams or clients. `/github/encode/httpx/tests/client/test_async_client.py` checks these contracts; published via `/github/encode/httpx/mkdocs.yml`.
