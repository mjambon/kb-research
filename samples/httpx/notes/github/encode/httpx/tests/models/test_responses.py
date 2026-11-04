# Verify responses behavior

tags: response streaming testing

Checks `/github/encode/httpx/httpx/_models.py` `Response` content, text, JSON, status errors, representations, elapsed time, and streaming access. Encoding cases cover charset headers, UTF-8 defaults, and callable detection behavior; the decoder implementation is in `/github/encode/httpx/httpx/_decoders.py`. Review these tests before changing how `.text`, `.content`, or iterators consume a body.
