# Declare package identity and version

tags: build api

Hatch reads the version from this module via `/github/encode/httpx/pyproject.toml`. The client uses `__version__` in its default User-Agent, and the public facade exports the identity values. The version synchronization script `/github/encode/httpx/scripts/sync-version` compares this value with `/github/encode/httpx/CHANGELOG.md`; review release changes across all three.
