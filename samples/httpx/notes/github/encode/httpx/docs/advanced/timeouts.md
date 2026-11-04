# Explain request timeout configuration

tags: config docs

This guide explains the default five-second network inactivity timeout, per-request and client defaults, disabling timeouts, and separate connect, read, write, and pool settings. `/github/encode/httpx/httpx/_config.py` defines `Timeout`; `/github/encode/httpx/httpx/_client.py` places its values in request extensions for the transport. `/github/encode/httpx/tests/test_timeouts.py` checks distinct failure types. `/github/encode/httpx/mkdocs.yml` publishes the page.
