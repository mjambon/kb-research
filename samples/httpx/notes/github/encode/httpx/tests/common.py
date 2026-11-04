# Share test constants and helper data

tags: testing

This module defines `TESTS_DIR` and `FIXTURES_DIR` from its own location so tests can locate committed fixture data without depending on the shell's working directory. It belongs to the test harness, not the installed HTTPX API; `/github/encode/httpx/tests/fixtures/` holds the netrc examples.
