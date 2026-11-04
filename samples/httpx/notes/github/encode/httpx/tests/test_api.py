# Verify api behavior

tags: api request testing

Checks top-level helpers in `/github/encode/httpx/httpx/_api.py` for request methods, body streams, response streaming, invalid URLs, and lazy loading of httpcore. This suite guards the convenience API exported by `/github/encode/httpx/httpx/__init__.py`; persistent client behavior has separate tests under `/github/encode/httpx/tests/client/`.
