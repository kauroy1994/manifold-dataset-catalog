# FF23-M · 2023 multimodal observations

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
| Formats reported | JSON, image batches |
| Reported multimodal records | 166,000 |
| Sampling rate | 2–3 Hz, as reported |
| Raw data included here | No |
| File-level audit | Not performed |

**Source:** Harik et al. (2024), [Analog and Multi-modal Manufacturing Datasets Acquired on the Future Factories Platform](https://arxiv.org/abs/2401.15544); PDF pp. 5–6, Section III(b). The dates in the catalog refer to data collection; the paper's year is different.

Sensor values linked to dual-view imagery Batched images and corresponding JSON records.

## All original download parts

| Published part | Original landing page | Kaggle dataset identifier |
|:--|:--|:--|
| 1 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-16) | `ramyharik/ff-2023-12-12-multi-modal-dataset-16` |
| 2 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-26) | `ramyharik/ff-2023-12-12-multi-modal-dataset-26` |
| 3 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-36) | `ramyharik/ff-2023-12-12-multi-modal-dataset-36` |
| 4 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-46) | `ramyharik/ff-2023-12-12-multi-modal-dataset-46` |
| 5 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-56) | `ramyharik/ff-2023-12-12-multi-modal-dataset-56` |
| 6 of 6 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2023-12-12-multi-modal-dataset-66) | `ramyharik/ff-2023-12-12-multi-modal-dataset-66` |

**URL source:** PDF p. 6, Download Links of the [publication PDF](https://arxiv.org/pdf/2401.15544). Parts are subdivisions of one asset, not independent datasets. Obtain files directly from the source and record the version you actually retrieve. Kaggle may require an account or agreement to its access conditions.

## Interpretation limits

- The approximately 166,000 records cover the complete multimodal asset, not each of its six parts.
- Do not assume every analog annotation can be transferred to an image without checking identifiers and time alignment.
- Repeated measurements within one cycle are not independent observations. The two campaigns share one testbed.
- Raw source file hashes, exact bytes, current downloadable versions, complete class counts, and source-level temporal alignment have not been audited in this planning repository.
- Do not convert a cycle-level component-omission label into a claim that a particular operation was skipped or failed.

## Proposed enhancement — not implemented

Evidence-preserving visual–sensor alignment and event grounding. This is a research objective, not an existing feature of this repository. [Research roadmap](../docs/roadmap.md).

## Licensing and verification

The paper reports **CC BY-SA 4.0** in its License section (PDF p. 6, License). This records the publication's statement, not an independent per-file license audit. See [licensing boundaries](../docs/licensing.md). Original creators retain credit; acquisition took place at the University of South Carolina.

**Checked 2026-10-24:** paper metadata and the published URL list; expected landing-page titles observed. **Not checked:** authenticated downloads, file integrity, class frequencies, consent documentation, or completed manufacturing validation. [Verification ledger](../docs/source-verification.md).
