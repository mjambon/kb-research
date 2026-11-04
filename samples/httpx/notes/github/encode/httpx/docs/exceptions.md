# Explain exceptions

tags: api docs error

Documents the HTTPX exception hierarchy and named errors, separating request failures, transport failures, protocol errors, and `HTTPStatusError` raised explicitly from a response. `/github/encode/httpx/httpx/_exceptions.py` defines the hierarchy, and `/github/encode/httpx/httpx/_transports/default.py` translates httpcore failures. `/github/encode/httpx/tests/test_exceptions.py` guards mapping coverage. Published via `/github/encode/httpx/mkdocs.yml`.
