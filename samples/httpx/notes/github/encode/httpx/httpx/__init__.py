# Expose the supported HTTPX API

tags: api

This package facade re-exports the selected public helpers, models, transports, errors, and configuration types from internal modules. Its explicit `__all__` is the contract checked by `test_all_imports_are_exported` in `/github/encode/httpx/tests/test_exported_members.py`. It also rebinds exported classes and functions to the `httpx` module for public presentation. The optional CLI import falls back to a useful installation error when CLI dependencies are absent; the console entry point in `/github/encode/httpx/pyproject.toml` calls `httpx:main`.
