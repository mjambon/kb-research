# Verify queryparams behavior

tags: request testing url

Checks that `/github/encode/httpx/httpx/_client.py` merges client-level query parameters with individual requests using `/github/encode/httpx/httpx/_urls.py` `QueryParams`. Cases cover object, string, and echo-server forms. The integration tests matter because normalized query values can differ from the raw input shape.
