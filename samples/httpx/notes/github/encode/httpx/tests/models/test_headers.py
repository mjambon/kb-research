# Verify headers behavior

tags: request response security testing

Checks `/github/encode/httpx/httpx/_models.py` `Headers` ordering, case-insensitive lookup, repeated fields, insertion, deletion, copying, and text encoding. Representation tests verify that sensitive header values are obfuscated. These invariants matter to both request construction and response interpretation.
