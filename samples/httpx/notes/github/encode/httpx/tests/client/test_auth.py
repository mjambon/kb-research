# Verify auth behavior

tags: auth security testing

Exercises client integration with `/github/encode/httpx/httpx/_auth.py` across Basic, Digest, netrc, URL credentials, custom flows, streaming, and disabling configured auth on one request. The tracked netrc examples in `/github/encode/httpx/tests/fixtures/` distinguish valid credentials from a parse error. These tests matter because auth generators can consume a response and issue another request; the client owns that lifecycle. Shared apps come from `/github/encode/httpx/tests/conftest.py`.
