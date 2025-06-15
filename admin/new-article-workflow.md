# Workflow: Adding a New Article with PDF

This guide explains the steps required to publish a new article and associated PDF in this repository.

## Manual vs Automated Steps

### Manual Steps (Done by User):
1. Place documents in `drafts/to-process/` folder
2. Ask Claude Code to process the documents
3. Review the processed documents
4. Handle all git operations (add, commit, push)
5. Add LinkedIn reference to front matter after posting

### Automated Steps (Done by Claude Code):
1. Check `drafts/to-process/` folder for new documents
2. Rename files to lowercase-dash format
3. Create date folders (using current date)
4. Move files to proper locations
5. Add front matter to markdown files
6. Update research index pages
7. Update homepage Latest Research section
8. Verify date accuracy and fix if needed

---

## 1. Clone the repository with the `files` submodule

```bash
git clone git@github.com:DinisCruz/docs.diniscruz.ai.git
cd docs.diniscruz.ai
# fetch PDF repository as submodule
git submodule update --init --recursive
```

The `files` directory contains PDFs and other binary assets. It is a separate repository referenced as a Git submodule.

## 2. Add the PDF to the submodule

**Note:** The PDF directory structure is `files/files/pdf/YYYY/MM/DD/` (not `github/pdf/`).

1. Navigate into the `files` folder.
2. Create the required date‑based directory structure if it doesn't exist. For example, to add a PDF dated `2025/06/05`, create `files/pdf/2025/06/05/`.
3. Move (not copy) your PDF into that folder.
4. Commit the change **inside the submodule**:

```bash
cd files
git checkout -b add-new-pdf
git add files/pdf/2025/06/05/my-document.pdf
git commit -m "Add PDF for 2025‑06‑05 article"
cd ..
```

The submodule commit will be referenced from the main repository after the next step.

## 3. Create the Markdown article

1. Inside `docs`, create a folder structure that matches the article date (`YYYY/MM/DD`).
2. Add a Markdown file with front‑matter fields similar to the examples under `docs/2025/`.
3. Set the `pdf_file` property to the PDF filename and the `date` property to the folder's date.
4. Immediately after the front matter, include:

    
```markdown
 _by {{ authors | join(" and ") }}, {{ date }}_

 {{ download_pdf(date, pdf_file) }} {{ linkedin_post(linkedin) }} {{back_button(back_link)}}
 ``` 

5. For presentations/slides: Insert `{{ view_pdf(date, pdf_file) }}` where you want the PDF to appear.
   For research documents with full content: Only use the download link at the top (no embedded viewer needed).
6. Do **not** include a top‑level `#` heading—the page title is automatically generated from the `title` value in the front matter.

Example front matter:

```markdown
---
title: "My New Presentation"
authors: ["Dinis Cruz"]
date: 2025/06/05
pdf_file: my-document.pdf
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

## Processing Research Documents from Drafts (Claude Code Workflow)

When processing research documents that include both PDF and markdown content, Claude Code will:

### 1. File naming convention
Convert filenames to lowercase with dashes instead of spaces:
- Original: `History and Analysis of OWASP In-Person Summits.pdf`
- Converted: `history-and-analysis-of-owasp-in-person-summits.pdf`

### 2. File placement
```bash
# Move markdown file (Claude Code will use the current date)
mv drafts/to-process/Document-Name.md docs/YYYY/MM/DD/document-name.md

# Move PDF file (create directory first)
mkdir -p files/files/pdf/YYYY/MM/DD/
mv drafts/to-process/Document-Name.pdf files/files/pdf/YYYY/MM/DD/document-name.pdf
```

**Important:** Files are MOVED, not copied, to avoid duplication.

### 3. Front matter for research documents
```markdown
---
title: "Document Title"
authors: ["Author Name"]
date: YYYY/MM/DD
pdf_file: document-name.pdf
back_link: /research/cyber-security
# linkedin: (add when post has been created in LinkedIn)
---

_by {{ authors | join(" and ") }}, {{ date }}_

{{ download_pdf(date, pdf_file) }} {{ linkedin_post(linkedin) }} {{back_button(back_link)}}

[Document content continues here...]
```

### 4. Key differences for research documents
- **No PDF viewer at the end**: Research documents with full markdown content don't need `{{ view_pdf() }}`
- **Full content in markdown**: The entire document text should be in the markdown file
- **Download link only**: The PDF download button at the top is sufficient

### 5. Update the research index
Claude Code will add the new article to the appropriate research page (e.g., `docs/research/cyber-security.md`) maintaining date order (newest first).

### 6. Update homepage Latest Research section
Claude Code will update the homepage (`docs/index.md`) to include the new article in the "Latest Research" section:
- Replace the oldest entry (4th item) with the new article
- Maintain the 4 most recent articles
- Include a brief one-line description of the article

Example update:
```markdown
### 🔥 Latest Research (June 2025)

- **[New Article Title](./2025/06/15/new-article-url.md)** - Brief description of the article
- **[Previous Article 1](./2025/06/14/...)** - Description
- **[Previous Article 2](./2025/06/13/...)** - Description  
- **[Previous Article 3](./2025/06/12/...)** - Description
```

### 7. Date handling
Claude Code will use the current date when processing documents. If the date is incorrect:
- Claude Code will create the correct date folders
- Move all files to the new location
- Update the front matter date
- Update all index references

## Common Research Sections and back_link Values

- **Cyber Security**: `/research/cyber-security`
- **Development and GenAI**: `/research/development-and-genai`
- **Europe and Learning**: `/research/europe-and-learning`
- **Graphs**: `/research/graphs`
- **Projects**: `/research/projects`
- **The Future of News**: `/research/the-future-of-news`

## Git Operations (Manual)

After Claude Code processes the documents:

1. Review the changes
2. Add and commit in the main repository:
   ```bash
   git add -A
   git commit -m "Added new research document: [title]"
   ```
3. If PDFs were added, also commit in the files submodule:
   ```bash
   cd files
   git add -A
   git commit -m "Added PDFs for new research documents"
   cd ..
   git add files
   git commit -m "Updated files submodule reference"
   ```
4. Push both repositories:
   ```bash
   git push
   cd files
   git push
   ```