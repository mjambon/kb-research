# Verify status codes behavior

tags: response testing

Checks `/github/encode/httpx/httpx/_status_codes.py` `codes` numeric values, names and aliases, reason phrases, and behavior for unknown status values. These are caller-facing classification helpers; response handling in `/github/encode/httpx/httpx/_models.py` depends on consistent status interpretation.
