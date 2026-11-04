# Explain authentication

tags: auth docs security

Describes Basic, Digest, netrc, and custom generator-based authentication. `/github/encode/httpx/httpx/_auth.py` implements the schemes, while `/github/encode/httpx/httpx/_client.py` drives a flow that can respond to challenges. The custom-flow examples are important because auth can require more than adding one header; `/github/encode/httpx/tests/client/test_auth.py` exercises client integration. Published via `/github/encode/httpx/mkdocs.yml`.
