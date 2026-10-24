# FF24-M · 2024 multimodal observations

**EXISTING UPSTREAM DATA · PUBLICATION-REPORTED CATALOG ENTRY**

[Back to dataset catalog](../README.md#dataset-catalog)

This card summarizes the original publication. It does not certify the downloadable file inventory, content quality, or permissions for every downstream use. No MANIFOLD-enhanced data are supplied.

## Reported source characteristics

| Field | Publication-reported value or catalog status |
|:--|:--|
| Acquisition campaign | August 2024 / Future Factories V2 |
| Acquisition site | Future Factories Laboratory, University of South Carolina |
| Duration reported | 8 hours |
| Campaign-level complete cycles | 93 |
| Formats reported | JSON, image batches |
| Reported multimodal records | 85,000 |
| Sampling rate | Not established here; do not infer from another asset |
| Raw data included here | No |
| File-level audit | Not performed |

**Source:** Harik et al. (2025), [Analog and Multi-modal Manufacturing Datasets Acquired on the Future Factories Platform V2](https://arxiv.org/abs/2502.05020); PDF pp. 3–4, Sections III and V(b–c). The dates in the catalog refer to data collection; the paper's year is different.

Dual-view image and sensor records Worker-safety observations reported in the collection.

## All original download parts

| Published part | Original landing page | Kaggle dataset identifier |
|:--|:--|:--|
| 1 of 3 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2024-08-13-multi-modal-dataset-13) | `ramyharik/ff-2024-08-13-multi-modal-dataset-13` |
| 2 of 3 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2024-08-13-multi-modal-dataset-23) | `ramyharik/ff-2024-08-13-multi-modal-dataset-23` |
| 3 of 3 | [Open original Kaggle page](https://www.kaggle.com/datasets/ramyharik/ff-2024-08-13-multi-modal-dataset-33) | `ramyharik/ff-2024-08-13-multi-modal-dataset-33` |

**URL source:** PDF p. 5, Download Links of the [publication PDF](https://arxiv.org/pdf/2502.05020). Parts are subdivisions of one asset, not independent datasets. Obtain files directly from the source and record the version you actually retrieve. Kaggle may require an account or agreement to its access conditions.

## Interpretation limits

- Approximately 85,000 records span the three parts together, not each part.
- Worker imagery requires privacy and redistribution review; publication availability is not a blanket clearance for every use.
- Label names here are transcribed from the paper, not reconciled with the distributed files.
- Repeated measurements within one cycle are not independent observations. The two campaigns share one testbed.
- Raw source file hashes, exact bytes, current downloadable versions, complete class counts, and source-level temporal alignment have not been audited in this planning repository.
- Do not convert a cycle-level component-omission label into a claim that a particular operation was skipped or failed.

## Proposed enhancement — not implemented

Source-linked multimodal events and privacy-aware safety-observation metadata. This is a research objective, not an existing feature of this repository. [Research roadmap](../docs/roadmap.md).

## Licensing and verification

The paper reports **CC BY-SA 4.0** in its License section (PDF p. 5, License). This records the publication's statement, not an independent per-file license audit. See [licensing boundaries](../docs/licensing.md). Original creators retain credit; acquisition took place at the University of South Carolina.

**Checked 2026-10-24:** paper metadata and the published URL list; expected landing-page titles observed. **Not checked:** authenticated downloads, file integrity, class frequencies, consent documentation, or completed manufacturing validation. [Verification ledger](../docs/source-verification.md).

## Label strings as reported in the paper

`No Nose`, `No Nose and No Body 2`, `No Nose, No Body 2, and No Body 1`, `Normal`.

These are publication-level spellings. Do not silently normalize them or assume exact equivalence to downloaded column values.
