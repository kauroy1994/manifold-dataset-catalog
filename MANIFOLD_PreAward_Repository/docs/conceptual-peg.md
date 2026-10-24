# Conceptual Process Event Graph

**DESIGN PREVIEW · NOT A FINAL ONTOLOGY OR VERIFIED DATA RELEASE**

[Return to MANIFOLD](../README.md) · [Open illustrative viewer](../examples/interactive_peg_viewer.html)

The proposed representation keeps manufacturing observations, deterministic derivations, model inferences, and nominal process rules distinguishable. Unknown information is not a failed observation and must not be silently completed from the expected procedure.

## Proposed record concepts

| Concept | Intended meaning | Status in this repository |
|:--|:--|:--|
| Source reference | Original dataset, file/record identifier, and authorized evidence location | Catalog-level paper links only; no verified cycle evidence |
| Execution | A particular manufacturing run or cycle | No actual source cycle selected |
| Event/state | What happened or what was observed, with component and interval | Schematic instances only |
| Assertion status | Observed, deterministically derived, model-inferred, normative, or illustrative | Illustrative status is explicit in the example |
| Validation status | Review outcomes and applicable checks, kept separate from assertion type | No manufacturing validation completed |
| Uncertainty | Unresolved content or timing; a score only when its meaning and estimation are documented | No invented scores or timestamps |
| Transformation lineage | Input references, code/model versions, reviewer decisions and permitted uses | Proposed research requirement |

This is a conceptual field guide, not a machine-enforced JSON Schema. Developing and validating the domain model remains proposed work. An accepted inference would still be an inference; review does not turn it into a raw observation.

## The NoNoseCone example

The source publication describes a `NoNoseCone` defect category. The example illustrates a missing-component interpretation at the category level and contrasts it with an expected installation operation. It does not identify an actual defective cycle, determine a missing-operation time, or establish whether installation was attempted, skipped, unsuccessful, or followed by later removal.

[Illustrative JSON-LD](../examples/illustrative_nose_cone.jsonld) uses an `example.org` namespace deliberately. `sourceCycleId` is null because no real source cycle has been verified. JSON null means an unspecified field in this illustrative document; JSON-LD/RDF processing may omit null values. A final unknown-value model is not specified here.

The expected operation is represented as a distinct JSON-LD resource with `fromState` and `toState` references. The viewer renders it as a labeled edge for readability; this is a visualization projection, not a claim that the entire future PEG schema consists only of states and transitions. Some display links reverse an underlying evidence reference; their inspectors identify the relationship as a display projection rather than a directly asserted source triple.

## Evidence needed for a real reconstruction

An actual example would require a stable source snapshot, a verified cycle identifier, original annotations, relevant sensor/image references, temporal alignment evidence, rights and privacy review, and documented validation outcomes. The current example supplies none of those as measured results.

## Source

Harik et al. (2024), [Future Factories dataset paper](https://arxiv.org/abs/2401.15544), Section III(a), for the documented defect category. The remaining instances are illustrative modeling choices supplied for the MANIFOLD planning discussion.
