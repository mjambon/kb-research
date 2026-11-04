# Explain environment variables

tags: config docs security transport

This guide describes proxy variables, `NO_PROXY`, `SSL_CERT_FILE`, and `SSL_CERT_DIR`, and shows that `trust_env=False` disables environment-based configuration. `/github/encode/httpx/httpx/_utils.py` parses proxy settings, `/github/encode/httpx/httpx/_client.py` uses them for routing, and `/github/encode/httpx/httpx/_config.py` reads certificate paths. `/github/encode/httpx/mkdocs.yml` publishes the page.
