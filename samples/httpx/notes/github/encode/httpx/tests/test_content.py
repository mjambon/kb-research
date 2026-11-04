# Verify content behavior

tags: request streaming testing

Checks `/github/encode/httpx/httpx/_content.py` encoding for empty, byte, sync/async iterator, JSON, URL-encoded, text, and multipart bodies. It also covers invalid argument combinations and response content encoding. These cases guard both the generated body and its headers; multipart details are tested in `/github/encode/httpx/tests/test_multipart.py`.
