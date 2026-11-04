# Verify decoders behavior

tags: response streaming testing

Checks `/github/encode/httpx/httpx/_decoders.py` deflate, zlib, gzip, Brotli, Zstandard, stacked encodings, text, and line decoding. Empty, truncated, malformed, and fragmented inputs are covered, including optional decoder behavior. This is the key test boundary for incremental `Response` reads in `/github/encode/httpx/httpx/_models.py`.
