# Verify cookies behavior

tags: request response testing

Checks `/github/encode/httpx/httpx/_models.py` `Cookies` creation, update, domain/path matching, multiple `Set-Cookie` values, list-of-pairs input, and representation. Domain and path cases matter when deciding which cookie is returned for a request; client persistence is covered separately in `/github/encode/httpx/tests/client/test_cookies.py`.
