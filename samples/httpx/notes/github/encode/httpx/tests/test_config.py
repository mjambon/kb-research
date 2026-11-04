# Verify config behavior

tags: config security testing

Checks `/github/encode/httpx/httpx/_config.py` SSL context creation from verification settings, CA files and directories, client cert/key pairs, encrypted keys, disabled verification, and environment key logging. It also tests `Limits`, `Timeout`, and `Proxy` construction and representations. These cases guard both security defaults and validation errors that occur before a network request.
