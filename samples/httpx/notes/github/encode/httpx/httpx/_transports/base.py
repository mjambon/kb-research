# Define synchronous and asynchronous transport interfaces

tags: api async transport

`BaseTransport.handle_request` and `AsyncBaseTransport.handle_async_request` accept a prepared `Request` and return a `Response`; close methods and context managers own transport resources. `/github/encode/httpx/httpx/_client.py` calls these interfaces and can mount custom implementations. Implementations in this folder must preserve stream ownership and the matching sync or async contract.
