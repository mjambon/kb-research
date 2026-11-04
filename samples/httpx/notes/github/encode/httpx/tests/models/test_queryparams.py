# Verify queryparams behavior

tags: testing url

Checks `/github/encode/httpx/httpx/_urls.py` `QueryParams` construction, repeated values, type coercion, immutability-oriented `set`, `add`, `remove`, and `merge` operations, and hashing. Tests explicitly reject the old mutating update and setter interfaces. Client-level merging is tested in `/github/encode/httpx/tests/client/test_queryparams.py`.
