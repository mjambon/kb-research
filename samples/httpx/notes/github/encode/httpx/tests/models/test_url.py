# Verify url behavior

tags: security testing url

Checks `/github/encode/httpx/httpx/_urls.py` `URL` construction, normalization, credentials, host and port validation, percent escapes, and path or query behavior. Lower-level parsing is in `/github/encode/httpx/httpx/_urlparse.py`. These cases are relevant to security-sensitive origin comparisons in `/github/encode/httpx/httpx/_client.py`; do not infer that a URL string comparison is equivalent to normalized origin comparison.
