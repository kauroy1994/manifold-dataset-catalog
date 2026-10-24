# Publish MANIFOLD from your personal GitHub account

This package is a **pre-award source catalog**, not a completed research platform. No content has been published on your behalf.

## 1. Review the public content

Read `README.md`, the team table, `docs/licensing.md`, and `DATA_GOVERNANCE.md`. Confirm that you have permission to publish the project description and proposed collaborator roles. Do not add the full proposal, budgets, private collaborator documents, raw data, worker images, or credentials.

The public site clearly distinguishes existing upstream data, conceptual examples, and planned research. Keep those labels intact. No external archival host, award, or pilot commitment is claimed.

## 2. Create an ordinary project repository

On your personal GitHub account, create a **public** repository. Suggested name: `manifold-dataset-catalog`.

This is a project website: do not rename or replace your personal profile repository or your existing personal website. Create the new repository empty, without generating another README or license.

Extract the ZIP and upload the **contents** of `MANIFOLD_PreAward_Repository`, not the ZIP itself and not an extra enclosing folder. In particular, preserve the hidden `.github` directory and `.gitignore`.

The repository root should contain `README.md`, `GETTING_STARTED.md`, `catalog/`, `docs/`, `examples/`, `assets/`, `site/`, `tools/`, `tests/`, and `.github/`.

### Option A: GitHub Desktop

Add the extracted folder as a local repository, create a repository there when prompted, and publish it to your account. Ensure that the repository visibility is public. Review the changed-file list, including `.github/workflows/`, before committing.

### Option B: Git command line

Run these commands from the extracted repository folder. Replace only the remote URL with the exact HTTPS URL displayed by GitHub for the empty repository you created.

```bash
git init -b main
git add .
git commit -m "Add MANIFOLD pre-award dataset catalog"
git remote add origin https://github.com/YOUR_USERNAME/manifold-dataset-catalog.git
git push -u origin main
```

`YOUR_USERNAME` above is an instruction variable, not a published site dependency. The site itself has no hard-coded GitHub owner or domain.

### Option C: Browser upload

Use **Add file → Upload files** and upload the extracted contents. Confirm that `.github/workflows/check.yml` and `.github/workflows/pages.yml` exist afterward. File pickers may hide dot-prefixed folders; GitHub Desktop or Git is more reliable. Uploading the ZIP as a single file will not publish its contents.

## 3. Enable the website

In the new repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Open **Actions → Publish documentation website → Run workflow**, choose `main`, and run it. The initial push may have tried to publish before Pages was enabled; rerun after enabling Pages. After deployment succeeds, GitHub's Pages settings and the workflow environment display the real site address.

For a normal project repository, the address has the form:

```text
https://YOUR_USERNAME.github.io/manifold-dataset-catalog/
```

Do not configure “Deploy from a branch” for the source repository unless you separately publish a built static directory. This package's normal route is the supplied GitHub Actions workflow.

The workflow does not require your Kaggle credentials, a custom domain, an API key, or an AI subscription. It downloads only the Python documentation-rendering dependencies.

## 4. Edit once, update both

Edit **README.md** to change the GitHub front page and website homepage. On a push to `main`, the workflow rebuilds the website. Edit the Markdown dataset cards and documents to change their corresponding website pages. The builder rewrites `.md` links to `.html` and keeps paths relative.

`catalog/datasets.json` and the human-readable cards must be updated together when source metadata changes. Record the evidence and review date in the ledger. A metadata correction is not a raw-file audit.

## 5. Preview locally

Use Python 3.10 or newer; the included workflow uses Python 3.12.

```bash
python -m pip install -r requirements-site.txt
python tools/check_repository.py
python -m unittest discover -s tests -v
python tools/build_site.py
python -m http.server 8000 --directory _site
```

Open `http://localhost:8000` in your browser. On Windows, replace `python` with `py` if that is how Python is installed. The package includes a prebuilt `_site/` for immediate local review, but `_site/` is ignored by Git because the workflow rebuilds it.

The test suite checks catalog bookkeeping, example consistency, page links and documentation rendering. It does not test manufacturing claims or authenticate upstream downloads.

## 6. Optional adjustments before publication

Enable Issues and private vulnerability reporting where available. The supplied issue forms collect catalog corrections and reuse interest, not raw datasets or sensitive evidence. Add the real website address to the repository's About panel after successful deployment. `CITATION.cff` intentionally omits an invented repository URL or DOI; add the actual repository URL after publication if desired.

## Troubleshooting

**404 page:** confirm the source is GitHub Actions, the deployment completed, and the URL includes the project-repository name. Do not assume the site lives at your account's domain root.

**Workflow fails before deployment:** check that Pages is enabled, GitHub Actions is permitted, the branch is `main`, and the complete hidden `.github` folder was uploaded.

**Viewer looks unstyled locally:** open it from `_site/examples/interactive_peg_viewer.html` with the full package intact, or use the local HTTP server. Keep the `assets/` directory alongside the site.

**README changed but website did not:** inspect the latest publication workflow run. The source README is not a second, separately maintained homepage.

**Catalog check reports an out-of-sync viewer:** after intentionally editing the example JSON-LD, regenerate the checked-in viewer with `python tools/sync_example.py`, then rerun the tests. This is a documentation operation, not evidence validation.

## Official deployment references

[GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [Custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
