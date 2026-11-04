# Explain event hooks

tags: api docs

This guide documents client-wide `request` hooks, called after request preparation and before sending, and `response` hooks, called after response headers arrive and before returning the response. It shows logging, status checks, and mutation use cases. Async clients require async hook functions. `/github/encode/httpx/httpx/_client.py` invokes hooks; `/github/encode/httpx/tests/client/test_event_hooks.py` checks error propagation and redirects. `/github/encode/httpx/mkdocs.yml` publishes the page.
