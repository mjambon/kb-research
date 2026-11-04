# Verify whatwg behavior

tags: security testing url

This parametrized test compares `/github/encode/httpx/httpx/_urlparse.py` `urlparse` with cases from `/github/encode/httpx/tests/models/whatwg.json`. It filters out fixture records marked as failures and skips two space-encoding cases in the test body. It also normalizes hostname case and empty query or fragment representations before comparing fields. Thus a passing run covers a selected set of WHATWG cases, not the complete fixture or the full URL standard.
