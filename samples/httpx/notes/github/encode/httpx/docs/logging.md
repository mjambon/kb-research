# Explain logging

tags: config docs

This guide shows Python logging configuration for request and connection activity, including `httpx` and underlying `httpcore` loggers. `/github/encode/httpx/httpx/_client.py` emits client request logs; `/github/encode/httpx/httpx/_transports/default.py` delegates network work to httpcore. Log output can change with the underlying dependency version, so the examples are diagnostic guidance rather than a stable logging API. `/github/encode/httpx/mkdocs.yml` publishes the page.
