# Implement the HTTPX package

tags: api async

The package facade exports helpers, clients, models, configuration, errors, and transports. `/github/encode/httpx/httpx/_client.py` coordinates request policy; `/github/encode/httpx/httpx/_models.py` owns request and response state; `/github/encode/httpx/httpx/_transports/` handles I/O. Low-level URL, body, decoder, auth, and utility modules support those layers. `/github/encode/httpx/tests/` checks contracts.
