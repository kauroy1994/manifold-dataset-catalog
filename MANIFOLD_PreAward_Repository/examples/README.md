# Illustrative graph example

[Return to MANIFOLD](../README.md)

Open [interactive_peg_viewer.html](interactive_peg_viewer.html) in a browser, or inspect [illustrative_nose_cone.jsonld](illustrative_nose_cone.jsonld).

This is a **hand-authored design preview** adapted from the project owner's supplied graph example. It does not reconstruct or validate a particular recorded cycle. Source-cycle IDs remain null; no sensor values, confidence scores, or timestamps have been introduced. The terms under `https://example.org/manifold/peg#` are conceptual, not an adopted ontology.

The display separates nominal procedure, a category-level component-absence interpretation, and unresolved installation status. A `NoNoseCone` category cannot determine whether installation was attempted, failed, skipped, or followed by later removal.

The viewer inspects a fixed embedded JSON document and exports that same document. It does not load upstream data, execute inference, verify sources, or test compliance with a finalized PEG schema. After editing the JSON-LD, run `python tools/sync_example.py` to update the checked-in viewer, then rebuild the website with `python tools/build_site.py`. The repository consistency check detects stale copies.
