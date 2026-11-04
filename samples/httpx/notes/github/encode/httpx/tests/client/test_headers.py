# Verify headers behavior

tags: request security testing

Checks default and per-request header merging in `/github/encode/httpx/httpx/_client.py` and multi-value behavior in `/github/encode/httpx/httpx/_models.py` `Headers`. Cases cover conflicts, updates, removing defaults, malformed values, Host construction, origin comparisons, and HTTPS redirect detection. Header and origin cases are relevant to credential forwarding and request correctness.
