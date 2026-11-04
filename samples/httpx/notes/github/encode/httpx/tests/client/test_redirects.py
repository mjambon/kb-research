# Verify redirects behavior

tags: auth request security testing

Exercises `/github/encode/httpx/httpx/_client.py` redirect policy across 301, 302, 303, relative and malformed locations, loops, maximum hops, and the `next_request` path when following is disabled. Credential forwarding tests distinguish same-origin redirects, cross-origin redirects, and HTTP-to-HTTPS upgrades; those cases guard against leaking `Authorization`. Sync and async paths are both represented. Shared apps and server fixtures come from `/github/encode/httpx/tests/conftest.py`.
