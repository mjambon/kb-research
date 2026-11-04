# Explain custom and built-in transports

tags: api docs transport

This guide explains the `transport=` and `mounts=` extension points, and covers direct HTTP, WSGI, ASGI, mock, and custom transports. `/github/encode/httpx/httpx/_transports/base.py` defines the interface; `/github/encode/httpx/httpx/_client.py` selects a mounted transport, and the implementations live in `/github/encode/httpx/httpx/_transports/`. The ASGI transport does not run application lifespan events, a distinction called out in the guide. `/github/encode/httpx/mkdocs.yml` publishes the page.
