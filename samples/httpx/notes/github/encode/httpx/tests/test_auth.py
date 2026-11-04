# Verify auth behavior

tags: auth security testing

Checks `/github/encode/httpx/httpx/_auth.py` Basic and Digest authentication algorithms and challenge handling. Cases include 200 and 401 responses, nonce counting, cookie changes, the older RFC 2069 form, and RFC 7616 MD5 and SHA-256 variants. Client orchestration is tested separately in `/github/encode/httpx/tests/client/test_auth.py`; use both when changing a flow.
