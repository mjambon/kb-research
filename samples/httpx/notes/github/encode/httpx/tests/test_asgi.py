# Verify asgi behavior

tags: async testing transport

Exercises `/github/encode/httpx/httpx/_transports/asgi.py` with ASGI apps: scope path and raw path, headers, body upload, response completion, disconnect behavior, and application exceptions before or after a response starts. These tests check the in-process async transport contract without using a network socket. The public use is described in `/github/encode/httpx/docs/advanced/transports.md`.
