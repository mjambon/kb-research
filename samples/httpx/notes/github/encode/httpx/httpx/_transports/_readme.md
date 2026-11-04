# Define and implement request transport boundaries

tags: api async transport

Base interfaces define sync and async send and close operations. Default transports adapt to httpcore; ASGI and WSGI dispatch in process; mock answers through a handler. `/github/encode/httpx/httpx/_client.py` chooses transports and manages response lifecycle.
