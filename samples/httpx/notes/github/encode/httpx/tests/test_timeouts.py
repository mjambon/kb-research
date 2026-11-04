# Verify timeouts behavior

tags: config testing transport

Checks read, write, connect, and pool timeout failures, plus request-specific timeout propagation on an async client. `/github/encode/httpx/httpx/_config.py` normalizes values and `/github/encode/httpx/httpx/_client.py` writes timeout extensions consumed by the transport. Distinct exception types matter to callers deciding whether and how to retry.
