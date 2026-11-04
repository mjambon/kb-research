# Explain response text decoding choices

tags: docs response

This guide explains how `Response.text` selects a character encoding from `Content-Type`, falls back to UTF-8 by default, and can use an explicit or callable default encoding. `/github/encode/httpx/httpx/_models.py` performs response decoding, while `/github/encode/httpx/httpx/_client.py` accepts the client default. `/github/encode/httpx/tests/models/test_responses.py` checks decoding cases. `/github/encode/httpx/mkdocs.yml` publishes the page.
