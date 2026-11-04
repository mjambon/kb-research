# Provide immutable URL and query parameter values

tags: url api request

`URL` wraps the parsed raw URL with normalized accessors and methods for copying or joining components. `QueryParams` is an immutable, ordered multi-dict preserving repeated keys with set, add, remove, and merge operations. Clients use both for base URL joining, proxy matching, and parameter merging; models store request URLs. `/github/encode/httpx/httpx/_urlparse.py` performs low-level validation. The URL and query tests under `/github/encode/httpx/tests/models/` cover normalization and repeated values.
