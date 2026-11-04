# Implement request authentication flows

tags: api auth security

`Auth` defines generator-based flows that can send a request, inspect a response, and send another request. `sync_auth_flow` and `async_auth_flow` adapt flows that need buffered request or response bodies. `BasicAuth` builds a Basic header; `NetRCAuth` looks up host credentials in netrc; `DigestAuth` parses a 401 challenge and computes a response with nonce counting and supported quality-of-protection and algorithms. `/github/encode/httpx/httpx/_client.py` drives the flow, so changes here affect retries and redirects. `/github/encode/httpx/tests/client/test_auth.py` and `/github/encode/httpx/tests/test_auth.py` cover integration and algorithms.
