# Validate transport configuration

tags: config security transport

`create_ssl_context` uses certifi by default, or `SSL_CERT_FILE` and `SSL_CERT_DIR` when `trust_env` permits. It accepts an explicit SSL context; `verify=False` disables hostname and certificate checks. String `verify` paths and the `cert` argument are deprecated in this revision. `Timeout` normalizes connect, read, write, and pool values and exports them as request extensions. `Limits` controls pool size and keepalive; `Proxy` parses a proxy URL and auth. `/github/encode/httpx/httpx/_client.py` passes these values to `/github/encode/httpx/httpx/_transports/default.py`. `/github/encode/httpx/tests/test_config.py` checks configuration and error behavior.
