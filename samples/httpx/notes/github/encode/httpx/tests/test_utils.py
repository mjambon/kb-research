# Verify utils behavior

tags: config testing transport url

Checks `/github/encode/httpx/httpx/_utils.py` byte/string conversion, environment proxy parsing, URL pattern matching and priority, and logging across a request and redirect chain. Pattern priority matters to `/github/encode/httpx/httpx/_client.py` transport selection; conversion tests guard odd encodings and byte-order marks.
