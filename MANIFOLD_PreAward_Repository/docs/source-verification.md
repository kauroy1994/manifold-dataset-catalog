# Source-verification ledger

**Review date: 2026-10-24. Scope: publications and published links, not a raw-data audit.**

[Return to MANIFOLD](../README.md)

## Primary sources checked

| Source | What was checked | Locator |
|:--|:--|:--|
| [Harik et al. 2024](https://arxiv.org/abs/2401.15544) | Title, complete author list, preprint date, original acquisition institution | arXiv record and paper title page |
| [2023 campaign paper PDF](https://arxiv.org/pdf/2401.15544) | 325 complete cycles, 10 Hz analog rate, approximately 166,000 multimodal records and 2–3 Hz multimodal rate | PDF p. 5, Section III |
| Same paper | One analog URL, six multimodal URLs, reported CC BY-SA 4.0 | PDF p. 6, Download Links and License |
| [Harik et al. 2025](https://arxiv.org/abs/2502.05020) | Title, complete author list, preprint date, acquisition institution and campaign date | arXiv record and paper title page |
| [2024 campaign paper PDF](https://arxiv.org/pdf/2502.05020) | 93 cycles, approximately 85,000 multimodal records, cycle-state feature, reported R02 sensor issue and worker-safety observations | PDF pp. 3–4, Sections III–V |
| Same paper | One analog URL, three multimodal URLs, reported license, 21 state descriptions | PDF p. 5, Download Links, License and Appendix A |

The PDF download lists and state table were inspected visually. Source facts are summarized rather than reproduced as screenshots. Original publication dates are not the collection dates: the papers were posted in 2024 and 2025 for the 2023 and 2024 campaigns, respectively.

## What the link check establishes

All **11 published Kaggle URLs** were located in the original papers. Web retrieval also returned matching dataset landing-page titles. The page bodies were not available as substantive extracted text, so this check does not certify a live archive inventory or displayed license field.

A per-link record is retained in [link-checks.json](../catalog/link-checks.json). `download_verified` and `raw_file_license_verified` are **false**, not missing or optimistically true.

## Not performed

No authenticated Kaggle download; no source-file checksums; no compressed/decoded size measurement; no class-frequency recount; no cross-modal matching audit; no cycle reconstruction; no privacy/consent review; no sensor calibration; no scientific validation; no full historical-version archive.

FF24 sampling rates are intentionally left unspecified in the catalog instead of copying FF23's rates. Public PDFs and repo pages are not a substitute for examining the files.

## Project-specific information

The proposed team, three research thrusts, use of Future Factories as the seed portfolio, and illustrative graph model follow the project owner's supplied MANIFOLD proposal and example HTML. They are proposed arrangements, not independently certified external commitments. The private proposal, budgets, prior-support drafts, and collaborator documents are not included in this repository.

## Website implementation references

- [GitHub: configuring a Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub: custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [markdown-it-py documentation](https://markdown-it-py.readthedocs.io/en/latest/using.html)

These are technical implementation references, not evidence of scientific progress.
