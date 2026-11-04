# Verify wsgi behavior

tags: testing transport

Exercises `/github/encode/httpx/httpx/_transports/wsgi.py` with WSGI applications, including request body transfer, streaming response iterables, exceptions, logging, server port, and protocol fields. These tests guard environ construction and iterable cleanup at the sync transport boundary. The public use is described in `/github/encode/httpx/docs/advanced/transports.md`.
