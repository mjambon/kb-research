# Verify event hooks behavior

tags: api testing

Checks `/github/encode/httpx/httpx/_client.py` request and response hooks in sync and async clients, including hook exceptions and redirects. A hook failure must propagate rather than silently continuing; redirect cases establish that hooks run for the requests and responses involved in a chain. Compare with the user-facing timing guidance in `/github/encode/httpx/docs/advanced/event-hooks.md`.
