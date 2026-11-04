# Verify exported members behavior

tags: api testing

Checks that every public member exposed by `/github/encode/httpx/httpx/__init__.py` appears in `__all__`. This protects the package facade and its documented import surface when adding or removing exports; it does not establish behavior of each exported member.
