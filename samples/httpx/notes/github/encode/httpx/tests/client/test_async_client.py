# Verify async client behavior

tags: api async request testing

Checks `/github/encode/httpx/httpx/_client.py` `AsyncClient` methods, request building, JSON and streamed bodies, transport context management, and closed-client behavior. Accessing streamed response content before reading and sending a synchronous stream through the async path are explicit error cases. Compare `/github/encode/httpx/tests/client/test_client.py` for policy shared with the synchronous client.
