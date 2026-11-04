# Provide one-shot request helpers

tags: api request

`request` creates a short-lived `/github/encode/httpx/httpx/_client.py` `Client`, sends a request, and returns the loaded response. `stream` holds the client open while the caller iterates the response in a context manager. Method helpers delegate with method-specific arguments; `get` and `head` do not accept request bodies. These helpers are exported by `/github/encode/httpx/httpx/__init__.py` and exercised by `/github/encode/httpx/tests/test_api.py`. Use a persistent client for pooling or shared configuration.
