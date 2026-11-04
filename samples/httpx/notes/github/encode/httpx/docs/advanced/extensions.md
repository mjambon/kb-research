# Explain extensions

tags: api docs request response

Documents request and response extension dictionaries for low-level transport metadata. Timeout settings travel in `Request.extensions`; response extensions carry transport information such as HTTP version and network stream. `/github/encode/httpx/httpx/_client.py` sets timeout extensions and `/github/encode/httpx/httpx/_transports/default.py` exchanges extension values with httpcore. Extensions are an integration boundary for custom transports; published via `/github/encode/httpx/mkdocs.yml`.
