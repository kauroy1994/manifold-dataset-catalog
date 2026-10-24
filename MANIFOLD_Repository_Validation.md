# MANIFOLD pre-award repository: delivery and verification report

Prepared 24 October 2026. Package version: `0.1.0-planning`.

## Delivered scope

A documentation-first, pre-award source catalog with a README-driven static website, four Future Factories dataset cards, 11 original published Kaggle URLs, two complete source-paper BibTeX entries, proposed research and governance documentation, and a hand-authored illustrative Process Event Graph viewer. All source data remain upstream. No raw manufacturing files, proposal PDFs, private files, trained models, scientific inference pipeline, or measured experimental results are included.

The GitHub repository and Pages site have **not** been published. No account was created or modified. Collaborator roles, project funding, archival arrangements, and external-user participation are not represented as confirmed institutional commitments.

## Checks completed

- Repository consistency check: passed (four assets, two campaigns, 11 unique source links, part counts, matching link ledger, preserved unverified status flags, example references and embedded JSON consistency).
- Python unittest suite: **15 tests passed**.
- Static website build: **18 HTML pages** generated from the README and supporting Markdown, plus the example viewer.
- All generated local links and HTML anchors resolved.
- Source-tree viewer links resolved separately.
- Python syntax checks and JavaScript syntax check passed.
- GitHub workflow and issue-template YAML parsed; citation metadata YAML parsed.
- Desktop Chromium render of all 18 pages: no detected page-level horizontal overflow or JavaScript page errors.
- Mobile Chromium checks of the homepage and viewer at 390 pixels: no detected page-level horizontal overflow. Wide tables intentionally use a contained horizontal scroll area.
- Viewer filters, accessible item selection, null source-cycle status display, zoom/reset, and export-handler JSON payload checked. Exported JSON matched the illustrative source JSON-LD exactly.

These are documentation/software checks, **not scientific data-validation results**.

## Browser-test boundary

This environment blocks navigation to local file/server URLs. Browser checks therefore rendered the exact built HTML in memory with local styles/scripts inlined. Static link resolution was checked independently against files on disk. The export handler's Blob payload was tested without navigating its download URL. A live GitHub Actions run, deployed website navigation, and end-to-end browser download remain to be checked after the owner publishes the repository. No test bypassed the environment's local-navigation restriction.

## Source-verification boundary

The two original arXiv records, relevant PDF pages, download lists and reported licenses were checked. All 11 Kaggle URLs appeared in the papers; page retrieval returned matching landing-page titles but not substantive current file inventories. No authenticated download, per-file license audit, file hash verification, image privacy clearance, cycle-label recount, temporal alignment audit, or experimental reconstruction was performed. Publication-reported counts and licenses are labeled accordingly. FF24 sampling rates remain unspecified rather than copied from FF23.

See `docs/source-verification.md` and `catalog/link-checks.json` for the retained provenance of these checks.

## Publishing

Open `GETTING_STARTED.md` inside the package. Extract the ZIP, publish the contents of `MANIFOLD_PreAward_Repository` as a new public project repository, preserve `.github`, and select **Settings → Pages → Build and deployment → Source: GitHub Actions**. Run **Publish documentation website** on `main`. The website homepage is built directly from `README.md`.

The prebuilt `_site/` folder is included for immediate inspection. It is ignored by Git because the workflow regenerates it. Only allowlisted public documentation and examples enter the website build.

## Before public release

Confirm collaborator/team wording and permission to publish the project description; review the proposed MIT scope for newly authored scaffolding. Preserve upstream license/attribution notices. Add real repository/site URLs to citation metadata only after publication. Do not turn illustrative assertions into verified claims or reinterpret documentation checks as completed proposed research.
