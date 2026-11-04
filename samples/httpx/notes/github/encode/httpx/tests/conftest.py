# Configure fixtures and local HTTP test servers

tags: testing

Pytest fixtures provide ASGI apps, test certificates, an HTTP server, and a clean environment for integration tests. `TestServer` starts and restarts the local service in a thread. Many client tests depend on these fixtures; changes can alter network, TLS, and timing behavior across the suite. Pytest settings live in `/github/encode/httpx/pyproject.toml`.
