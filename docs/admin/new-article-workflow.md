# Workflow: Adding a New Article with PDF

This guide explains the steps required to publish a new article and associated PDF in this repository.

## 1. Clone the repository with the `files` submodule

```bash
git clone git@github.com:DinisCruz/docs.diniscruz.ai.git
cd docs.diniscruz.ai
# fetch PDF repository as submodule
git submodule update --init --recursive
```

The `files` directory contains PDFs and other binary assets. It is a separate repository referenced as a Git submodule.

## 2. Add the PDF to the submodule

1. Navigate into the `files` folder.
2. Create the required date‑based directory structure if it doesn't exist. For example, to add a PDF dated `2025/06/05`, create `github/pdf/2025/06/05/`.
3. Copy your PDF into that folder.
4. Commit the change **inside the submodule**:

```bash
cd files
git checkout -b add-new-pdf
git add github/pdf/2025/06/05/my-document.pdf
git commit -m "Add PDF for 2025‑06‑05 article"
cd ..
```

The submodule commit will be referenced from the main repository after the next step.

## 3. Create the Markdown article

1. Inside `docs`, create a folder structure that matches the article date (`YYYY/MM/DD`).
2. Add a Markdown file with front‑matter fields similar to the examples under `docs/2025/`.
3. Set the `file_name` property to the PDF filename and the `date` property to the folder's date.
4. Immediately after the front matter, include:

    
```markdown
 _by {{ authors | join(" and ") }}, {{ date }}_

 {{ download_pdf(date, pdf_file) }} {{ linkedin_post(linkedin) }} {{back_button(back_link)}}
 ``` 

5. Insert `{{ view_pdf(date, file_name) }}` where you want the PDF to appear, or use `{{ download_pdf(date, file_name) }}` for a simple download link.
6. Do **not** include a top‑level `#` heading—the page title is automatically generated from the `title` value in the front matter.

Example front matter:

```markdown
---
title: "My New Presentation"
authors: ["Dinis Cruz"]
date: 2025/06/05
file_name: my-document.pdf
back_link: /resources/presentations
youtube_id: <optional>
---
```

## 4. Update indexes

Add a link to the new article in `docs/resources/presentations.md` (or other relevant index pages).

## 5. Commit and push

After adding the article and updating the submodule reference, commit the changes in the main repository:

```bash
git add docs/resources/presentations.md docs/2025/06/05/my-new-presentation.md files
git commit -m "Add article and PDF for 2025‑06‑05"
```

Finally push the main repository and the submodule to GitHub.

