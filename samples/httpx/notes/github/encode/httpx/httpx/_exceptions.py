# Define HTTPX error boundaries

tags: api error transport

The hierarchy separates request and transport failures from response status errors, invalid URLs, and stream misuse. `HTTPError.request` lets consumers identify the request involved; `HTTPStatusError` carries a response after `raise_for_status`. The `request_context` helper attaches request context when lower layers raise. `/github/encode/httpx/httpx/_transports/default.py` maps httpcore exceptions into this public hierarchy; `/github/encode/httpx/tests/test_exceptions.py` checks mapping and request attachment.
