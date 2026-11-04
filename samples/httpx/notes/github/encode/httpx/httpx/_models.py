# Represent HTTP requests and responses

tags: api request response streaming security

`Headers` preserves repeated fields while offering case-insensitive access and redacts sensitive values in representations. `Request` normalizes URL, headers, and encoded body; `Response` owns streaming reads, content decoding, text encoding, JSON, status checks, history, and elapsed time. `Cookies` wraps a cookie jar with domain and path aware lookup. These models are shared by clients, transports, and the public API. Streaming state errors prevent consuming or reading bodies in invalid states; review `/github/encode/httpx/tests/models/` for edge contracts.
