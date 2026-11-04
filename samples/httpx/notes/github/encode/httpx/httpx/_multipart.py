# Serialize multipart form fields and uploads

tags: request streaming

`DataField` and `FileField` render form parts with safe header formatting, inferred media type, and byte data. `MultipartStream` computes a length when possible or supports chunked transfer and yields the boundary-delimited body in sync or async mode. `/github/encode/httpx/httpx/_content.py` chooses this encoder for files and mixed form data; `/github/encode/httpx/tests/test_multipart.py` covers boundaries, names, files, and headers.
