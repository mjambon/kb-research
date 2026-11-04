# Provide a backend-neutral test sleep helper

tags: async testing

The async `sleep` helper supports timing and concurrency tests across supported async backends. `/github/encode/httpx/tests/conftest.py` configures the suite; use this helper in tests that should not assume one event loop implementation.
