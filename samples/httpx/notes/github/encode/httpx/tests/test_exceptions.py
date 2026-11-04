# Verify exceptions behavior

tags: error testing transport

Checks `/github/encode/httpx/httpx/_transports/default.py` httpcore-to-HTTPX exception mapping and request attachment in `/github/encode/httpx/httpx/_exceptions.py`. The completeness test compares mapping coverage with httpcore exception classes, so new lower-layer exceptions need an intentional public error mapping. This module is a focused guard for the error boundary exposed to callers.
