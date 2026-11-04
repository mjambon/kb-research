# Verify requests behavior

tags: request streaming testing

Checks `/github/encode/httpx/httpx/_models.py` `Request` construction and body state: content length versus transfer encoding, encoded form and JSON data, host and accept-encoding overrides, and sync or async stream reading. Tests that reject content access before reading are important for preserving streaming semantics. Body encoding is implemented in `/github/encode/httpx/httpx/_content.py`.
