# Define body stream protocols and public input types

tags: api async streaming

`SyncByteStream` and `AsyncByteStream` specify iterable content plus cleanup. Type aliases describe accepted auth, timeout, proxy, URL, header, cookie, and request body inputs across the public API. Runtime code in `/github/encode/httpx/httpx/_client.py`, `/github/encode/httpx/httpx/_models.py`, and transports implements these shapes; changing aliases should follow actual coercion behavior.
