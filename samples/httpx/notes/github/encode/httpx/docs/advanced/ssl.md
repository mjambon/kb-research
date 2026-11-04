# Explain HTTPS certificate verification

tags: config docs security

This guide explains HTTPS certificate verification, custom CA stores, explicit SSL contexts, client certificates, and disabling verification. `/github/encode/httpx/httpx/_config.py` `create_ssl_context` implements the settings, with network transport use in `/github/encode/httpx/httpx/_transports/default.py`. Certificate verification is enabled by default; disabling it changes the trust boundary. At this revision, string `verify` paths and the `cert` argument remain supported but deprecated. `/github/encode/httpx/tests/test_config.py` checks SSL configuration and failures. `/github/encode/httpx/mkdocs.yml` publishes the page.
