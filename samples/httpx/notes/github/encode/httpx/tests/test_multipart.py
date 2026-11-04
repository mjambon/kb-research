# Verify multipart behavior

tags: request streaming testing

Checks `/github/encode/httpx/httpx/_multipart.py` boundary selection, content-type headers, invalid field names or values, file tuples, Unicode content, inferred media types, and length or streaming behavior. These cases guard wire-format correctness for file uploads created by `/github/encode/httpx/httpx/_content.py`.
