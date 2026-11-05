OCaml comments were replaced by spaces using 'ocom' (repo by mjambon).

The answer injected into Anchor.ml for "cm+answer" is:

(*
   Known issues:

   - An unrelated edit can move an anchor to a duplicate in another
     file. Candidates are ranked by matching text and then document ID,
     with no preference for the anchor's current document. If a copy was
     indexed first, editing bytes outside an intact anchored span can
     move the anchor to that copy.

   - Relocation can hide a later stale anchor from review. Relocation
     preserves [acknowledged_revision] while changing documents. If an
     acknowledged anchor moves from a high revision document to one at
     revision 0, a failed relocation at revision 1 remains
     [needs_review = false] until the new document exceeds the old
     acknowledgment number.

   - Matches can cross source boundaries. Candidate collection
     searches the global shingle index without checking the anchor's
     source. Deleting text in one repository can attach its anchor to an
     identical, unrelated snippet in another registered source.

   - Repeated text can become stale after an unrelated edit. Indexing
     discards every occurrence of a repeated shingle. A short anchor
     whose text appears twice in its document can therefore have no hits
     even when both copies remain intact.
*)

