# Send sync requests directly into a WSGI application

tags: api transport

`WSGITransport` builds a WSGI environ from the request, passes body and headers to the app, and converts `start_response` output into a `Response`. `WSGIByteStream` closes the app iterable when the response stream closes; leading empty chunks are skipped before status construction. App exception handling is configurable. `/github/encode/httpx/tests/test_wsgi.py` covers environ, streaming, and errors.
