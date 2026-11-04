# Verify cookies behavior

tags: request response testing

Checks cookie storage and persistence across `/github/encode/httpx/httpx/_client.py` requests using the `/github/encode/httpx/httpx/_models.py` `Cookies` wrapper and standard cookie jars. A dedicated test verifies that per-request `cookies=` emits a deprecation warning. This distinction matters when changing client defaults versus response cookie persistence.
