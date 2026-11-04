# Decode HTTP bodies incrementally

tags: response streaming

Content decoders implement `decode` and `flush` for identity, deflate, gzip, optional Brotli, and optional Zstandard encodings. `MultiDecoder` unwinds stacked content encodings; chunk, text, and line decoders support response iterators without requiring one full body conversion. `/github/encode/httpx/httpx/_models.py` selects these decoders for `Response`, while `/github/encode/httpx/httpx/_client.py` advertises available encodings. Preserve streaming and flush behavior when changing a decoder; `/github/encode/httpx/tests/test_decoders.py` covers malformed and fragmented input.
