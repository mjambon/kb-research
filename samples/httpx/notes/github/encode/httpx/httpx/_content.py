# Encode request and response body streams

tags: async request streaming

The encoding helpers choose among bytes, iterators, form data, multipart files, text, HTML, and JSON, returning a byte stream with content headers. `IteratorByteStream` and `AsyncIteratorByteStream` enforce the matching iteration mode. `encode_request` is used by `/github/encode/httpx/httpx/_models.py` `Request`; multipart work delegates to `/github/encode/httpx/httpx/_multipart.py`. `UnattachedStream` prevents a deserialized object from pretending its original stream is still available. `/github/encode/httpx/tests/test_content.py` checks payload and header behavior.
