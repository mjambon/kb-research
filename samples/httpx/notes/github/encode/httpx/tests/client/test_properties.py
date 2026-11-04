# Verify properties behavior

tags: api testing

Checks that `/github/encode/httpx/httpx/_client.py` exposes and updates base URL, headers, cookies, timeout, event hooks, and `trust_env` consistently. Base URL tests cover input with and without a trailing slash, which affects relative request joining. These tests guard mutable client configuration rather than one-shot helpers.
