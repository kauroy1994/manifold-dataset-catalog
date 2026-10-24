# Accessing the original Future Factories data

[Return to the catalog](../README.md#dataset-catalog)

## Use the upstream repositories

Open the dataset card for the asset you need and follow its original Kaggle links. FF23-M comprises six parts; FF24-M comprises three. Do not treat parts as independent experiments or multiply the reported record count by the number of parts.

This repository does not mirror the original CSV, JSON sensor records, or image collections. Catalog JSON contains descriptions and links, not the manufacturing observations themselves. There is no bulk downloader here and no requirement to provide credentials to MANIFOLD.

## Record your own access evidence

When retrieving data, record the actual upstream version, access date, file inventory, checksums, license terms and attribution requirements. Preserve original filenames and identifiers. Check that every multipart archive is present, then reconcile analog/multimodal identifiers before aligning annotations or making evaluation splits.

Kaggle controls authentication, access terms and availability. The web checks performed for this catalog observed landing-page titles but did not authenticate, download archives or establish current file inventories. A working link is not proof that a particular file is unchanged or currently downloadable.

## Do not commit downloaded data

Keep raw data, credentials, restricted imagery, and unpublished annotations outside this repository. `.gitignore` excludes common local data and credential paths but is not a substitute for reviewing each commit. Do not place Kaggle tokens in a public issue, notebook output, screenshot, or GitHub Actions log.

## Preserve scope and provenance

Both campaigns were acquired at the University of South Carolina. The proposed enhancement consortium has different current affiliations; a new repository does not transfer dataset ownership or imply institutional permission. See [licensing](licensing.md) before redistribution or public derivative releases.
