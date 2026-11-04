# Explain clients

tags: api docs request

Explains why persistent `Client` instances pool connections and keep cookies, then how shared headers, parameters, authentication, and other settings merge with a request. It also covers prepared requests and download progress. `/github/encode/httpx/httpx/_client.py` supplies these contracts, including the distinction between `build_request` and `send`; `/github/encode/httpx/tests/client/test_client.py` checks URL and configuration merging. Published via `/github/encode/httpx/mkdocs.yml`.
