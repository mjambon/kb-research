# Provide URL pattern and conversion utilities

tags: url config transport

`URLPattern` matches scheme, host, subdomains, and port and defines priority for mounts and proxies. `get_environment_proxies` translates proxy variables and bypass rules; primitive byte/string helpers support URL and header handling. `/github/encode/httpx/httpx/_client.py` uses pattern ordering when choosing transports. `/github/encode/httpx/tests/test_utils.py` verifies environment and matching behavior.
