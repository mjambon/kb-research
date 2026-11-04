# Parse and normalize URL components

tags: url security

`urlparse` validates scheme, authority, userinfo, host, port, path, query, and fragment into `ParseResult`. Helpers encode IDNA/IP hosts, normalize default ports and dot segments, and preserve valid percent escapes. `/github/encode/httpx/httpx/_urls.py` uses this parser to construct immutable URL values; `/github/encode/httpx/tests/models/test_url.py` and `/github/encode/httpx/tests/models/test_whatwg.py` cover validation and conformance cases. URL normalization affects origin checks in `/github/encode/httpx/httpx/_client.py`.
