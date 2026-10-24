# FF23-A · 2023 analog observations

**EXISTING UPSTREAM DATA · PUBLICATION-REPORTED CATALOG ENTRY**

[Back to dataset catalog](../README.md#dataset-catalog)

This card summarizes the original publication. It does not certify the downloadable file inventory, content quality, or permissions for every downstream use. No MANIFOLD-enhanced data are supplied.

## Reported source characteristics

| Field | Publication-reported value or catalog status |
|:--|:--|
| Acquisition campaign | December 2023 / Future Factories V1 |
| Acquisition site | Future Factories Laboratory, University of South Carolina |
| Duration reported | 30 hours |
| Campaign-level complete cycles | 325 |
| Formats reported | CSV |
| Reported multimodal records | Not applicable to this catalog item |
| Sampling rate | 10–10 Hz, as reported |
| Raw data included here | No |
| File-level audit | Not performed |

**Source:** Harik et al. (2024), [Analog and Multi-modal Manufacturing Datasets Acquired on the Future Factories Platform](https://arxiv.org/abs/2401.15544); PDF p. 5, Section III(a). The dates in the catalog refer to data collection; the paper's year is different.

Cycle-level missing-component annotations Sensor streams from the manufacturing assembly/disassembly experiment.

## All original download parts

| Published part | Original landing page | Kaggle dataset identifier |
|:--|:--|:--|
| 1 of 1 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-analog-dataset) | `ramyharik/ff-2023-12-12-analog-dataset` |

**URL source:** PDF p. 6, Download Links of the [publication PDF](https://arxiv.org/pdf/2401.15544). Parts are subdivisions of one asset, not independent datasets. Obtain files directly from the source and record the version you actually retrieve. Kaggle may require an account or agreement to its access conditions.

## Interpretation limits

- 325 is a campaign-level count, not an independent additional set of 325 multimodal executions.
- Published anomaly labels are not validated operation-level event annotations.
- Repeated measurements within one cycle are not independent observations. The two campaigns share one testbed.
- Raw source file hashes, exact bytes, current downloadable versions, complete class counts, and source-level temporal alignment have not been audited in this planning repository.
- Do not convert a cycle-level component-omission label into a claim that a particular operation was skipped or failed.

## Proposed enhancement — not implemented

Source-linked process-stage annotations and anomaly-to-evidence associations. This is a research objective, not an existing feature of this repository. [Research roadmap](../docs/roadmap.md).

## Licensing and verification

The paper reports **CC BY-SA 4.0** in its License section (PDF p. 6, License). This records the publication's statement, not an independent per-file license audit. See [licensing boundaries](../docs/licensing.md). Original creators retain credit; acquisition took place at the University of South Carolina.

**Checked 2026-10-24:** paper metadata and the published URL list; expected landing-page titles observed. **Not checked:** authenticated downloads, file integrity, class frequencies, consent documentation, or completed manufacturing validation. [Verification ledger](../docs/source-verification.md).

## Label strings as reported in the paper

`NoNoseCone`, `NoBody2,NoNose`, `NoBody1,NoBody2,NoNose`.

These are publication-level spellings. Do not silently normalize them or assume exact equivalence to downloaded column values.
