# Verify client behavior

tags: api request testing

Checks `/github/encode/httpx/httpx/_client.py` `Client` methods, request construction, streaming, status errors, base URL joining, transport context management, and lifecycle behavior. URL merge tests include absolute, relative, dotted, and colon-containing paths, which matter when changing `build_request`. `/github/encode/httpx/tests/client/test_async_client.py` covers the parallel async path.
