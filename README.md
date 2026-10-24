# MANIFOLD

[![GitHub repository](https://img.shields.io/badge/GitHub-View%20repository-181717?logo=github&logoColor=white)](https://github.com/kauroy1994/manifold-dataset-catalog)

**Existing manufacturing datasets. A transparent research roadmap.**

Process-grounded enhancement for reusable manufacturing science. 

> **PRE-AWARD PLANNING · SOURCE CATALOG**  
> This repository catalogs previously published Future Factories data and presents MANIFOLD's proposed enhancement research. It is **not** a release of enhanced datasets, a validated event-extraction system, or an NSF-funded project announcement. The graph example is illustrative; no recorded manufacturing cycle has been reconstructed or scientifically validated here.

[Explore the dataset catalog](#dataset-catalog) · [Open the illustrative graph](examples/interactive_peg_viewer.html) · [Read the research roadmap](docs/roadmap.md)

**Four source assets · Two collection campaigns · One testbed**

## Dataset catalog

The initial portfolio comes from the **Future Factories Laboratory at the University of South Carolina**. The original papers describe December 2023 and August 2024 campaigns on an industrial robotic assembly/disassembly testbed. MANIFOLD is a proposed **University of Alabama–led enhancement effort**, not the original data-collection project. Ramy Harik's current Clemson affiliation does not change the acquisition provenance. See the [2024 paper](https://arxiv.org/abs/2401.15544) and [2025 V2 paper](https://arxiv.org/abs/2502.05020).

| Source asset | Publication-reported scope | Existing observations | Access |
|:--|:--|:--|:--|
| **FF23-A** · 2023 analog | 325 retained complete cycles; 10 Hz | Sensor streams; cycle-level component-omission labels | [Dataset card & upstream link](catalog/ff23-analog.md) |
| **FF23-M** · 2023 multimodal | Approximately 166,000 records; 6 download parts | Two camera views with synchronized sensor records | [Dataset card & all 6 parts](catalog/ff23-multimodal.md) |
| **FF24-A** · 2024 analog | 93 complete cycles; 21 documented cycle states | Sensor streams; cycle-state feature; documented R02 sensor malfunction | [Dataset card & upstream link](catalog/ff24-analog.md) |
| **FF24-M** · 2024 multimodal | Approximately 85,000 records; 3 download parts | Dual-view images, sensor records, worker-safety observations | [Dataset card & all 3 parts](catalog/ff24-multimodal.md) |

**Read the counts correctly.** Analog and multimodal assets from the same campaign overlap in experimental provenance. They are not four independent factories. Record counts are reported by the papers, not new MANIFOLD measurements; complete inventories, file hashes, exact cross-modal matches, and class distributions remain unaudited. The [machine-readable catalog](catalog/datasets.json) records these limitations explicitly.

Source records remain at the original Kaggle repositories. This repository supplies **all 11 published upstream links**, not raw sensor files or images. Landing-page titles and paper-listed URLs were checked on **24 October 2026**; authenticated downloads and per-file license audits were not performed. See [source verification](docs/source-verification.md) and the [access guide](docs/access.md).

## What exists now

| Available in this repository | What it demonstrates | What it does not establish |
|:--|:--|:--|
| Source catalog, four dataset cards, and original citations | A documented existing-data starting point | A newly collected or enhanced dataset |
| Conceptual PEG vocabulary and illustrative JSON-LD | A proposed way to separate observations, inferences, and expectations | A finalized ontology or verified process reconstruction |
| Interactive example viewer | Inspection of a small hand-authored graph and its qualifiers | Automated extraction, scientific verification, or deployment at scale |
| Research roadmap and draft governance principles | Planned work and explicit release boundaries | Completed experiments, secured partnerships, or archival commitments |
| Website build and repository checks | Documentation consistency and functioning navigation | Manufacturing-data quality or research performance |

**The substantive research remains proposed:** event extraction, temporal harmonization, process-aware verification, graph-learning evaluation, expert audit, scientific benchmarks, independent reuse, and sustained community infrastructure.

## Research roadmap

MANIFOLD proposes to transform fragmented observations into interoperable, source-linked process resources. AI methods are candidate transformation mechanisms; **reusable data products and independently supported scientific use are the intended outcomes**.

| Proposed thrust | Dataset value to investigate | Planned evidence of value |
|:--|:--|:--|
| **T1 · Evidence-bounded enhancement** | Align records, propose events, and preserve uncertainty and source links | Event fidelity, alignment error, unsupported claims, and review effort |
| **T2 · Process-grounded representations** | Publish inspectable Process Event Graphs and evaluate optional learned views | Preservation of process/evidence queries, transfer, and resource cost |
| **T3 · Verifiable scientific use** | Support evidence-grounded inquiry and recognize missing information | Held-out analyses, appropriate abstention, and independent reproducibility |

The proposed 36-month sequence moves from source inventory and baseline releases to evaluated enhancements and independent reuse. It is **not an award start date or a promise of completed milestones**. [Read the roadmap and release boundaries](docs/roadmap.md).

## Illustrative process graph

A `NoNoseCone` category can motivate a component-absence example, but it does **not** establish that installation was skipped, failed, or even attempted in a particular cycle. Our hand-authored example keeps that operation status unresolved and leaves source-cycle identifiers unset.

[Open the interactive design preview](examples/interactive_peg_viewer.html) · [Inspect the illustrative JSON-LD](examples/illustrative_nose_cone.jsonld) · [Read the modeling notes](docs/conceptual-peg.md)

The viewer supports selecting graph items, inspecting properties, filtering relationship types, and exporting the example. It runs on a static page without an AI service or factory connection. **Its interface behavior is not preliminary evidence of successful dataset enhancement.**

## Proposed team

| Investigator | Institution stated in the proposal | Planned contribution |
|:--|:--|:--|
| **Kaushik Roy · Lead PI** | The University of Alabama | Scientific integration, process-grounded enhancement, verification |
| Manas Gaur | University of Maryland, Baltimore County | Semantic harmonization and interoperable access |
| Ramy Harik | Clemson University | Manufacturing validity and contributor engagement |
| Srinivasan Parthasarathy | The Ohio State University | Scalable graph representations and evaluation |
| Sudip Mittal | The University of Alabama | Provenance, security, and contribution integrity |

This is the proposed consortium, not a declaration of institutional funding or hosting commitments. **Original Future Factories acquisition: University of South Carolina.** [Clemson Composites](https://clemsoncomposites.com/) is a current institutional context, not the upstream host of these two collection campaigns.

## Responsible reuse

Both source publications report **CC BY-SA 4.0** for their datasets. Users must inspect the terms attached to the actual source release, retain attribution, and evaluate applicable privacy and other permissions. Worker imagery warrants particular care. See the [upstream license deed](https://creativecommons.org/licenses/by-sa/4.0/) and [licensing boundaries](docs/licensing.md).

The MIT license for newly authored repository scaffolding does **not** relicense upstream data, articles, images, or contributors' material. No raw source data or source-paper figures are redistributed here.

Corrections to catalog metadata and documented reuse needs are welcome through the repository's Issues tab. Do not submit personal data, raw worker images, credentials, or restricted industrial records. [Contribution guide](CONTRIBUTING.md) · [Draft governance](DATA_GOVERNANCE.md) · [Security reporting](SECURITY.md)

## Publications and citation

**Harik et al. (2024).** *Analog and Multi-modal Manufacturing Datasets Acquired on the Future Factories Platform.* arXiv:2401.15544. [Paper](https://arxiv.org/abs/2401.15544)

**Harik et al. (2025).** *Analog and Multi-modal Manufacturing Datasets Acquired on the Future Factories Platform V2.* arXiv:2502.05020. [Paper](https://arxiv.org/abs/2502.05020)

Use the original papers when citing the underlying datasets. [Complete BibTeX entries](references.bib) · [Catalog citation metadata](CITATION.cff). Citing this catalog does not replace attribution to the original data creators.

## Run or publish this website

**`README.md` is the homepage source.** A small documentation-only builder renders this file and the supporting Markdown pages into a static website. No AI models, data downloads, or dataset-processing services run during the build.

```bash
python -m pip install -r requirements-site.txt
python tools/check_repository.py
python -m unittest discover -s tests -v
python tools/build_site.py
python -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. For your personal GitHub profile, create a public project repository, push these files, and choose **Settings → Pages → Source: GitHub Actions**. The supplied workflow builds the site from this README. [Step-by-step setup, including Windows](GETTING_STARTED.md).

**Status:** `0.1.0-planning`. This site documents a proposed research direction; it does not imply NSF funding, endorsement, completed enhancements, guaranteed source availability, or secured external reuse partnerships.
