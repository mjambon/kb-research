# Automate contributor checks and releases

tags: build

Shell wrappers install dependencies, check formatting/types, run tests and coverage, build docs and distributions, and publish releases. GitHub workflows invoke them; `/github/encode/httpx/pyproject.toml` and `/github/encode/httpx/requirements.txt` provide their configuration.
