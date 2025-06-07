# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a MkDocs-based documentation site for Dinis Cruz's documents and research, deployed to AWS S3 and CloudFront. The site uses custom macros and plugins to embed PDFs, videos, and other media.

## Commands

### Local Development
```bash
# Install dependencies
pip install -e ".[docs]"

# Run local server
mkdocs serve -a localhost:8111

# Build the site
mkdocs build --clean
```

### Git Workflow
```bash
# Merge dev into main (use the shell script)
./gh_merge_into_main.sh
```

## Architecture

### Key Components

1. **MkDocs Configuration** (`mkdocs.yml`): Uses Material theme with custom plugins including `awesome-pages`, `macros`, and a custom footer plugin.

2. **Macros System** (`main.py`): Defines custom macros for embedding content:
   - `download_pdf()`: Creates PDF download buttons
   - `view_pdf()`: Embeds PDF viewer
   - `linkedin_post()`: Links to LinkedIn posts
   - `show_youtube()`: Embeds YouTube videos
   - `show_spotify_ui()`: Embeds Spotify podcasts
   - `show_infographic()`: Embeds infographic PDFs
   - `show_slides()`: Embeds presentation PDFs

3. **Files Submodule**: Binary assets (PDFs, images) are stored in a separate repository linked as a git submodule at `./files`.

4. **CI/CD Pipeline**:
   - **Dev branch**: Auto-deploys to S3 with minor version increment
   - **Main branch**: Auto-deploys to S3 with major version increment
   - Uses GitHub Actions with custom actions for deployment

### Content Structure

Articles are organized by date: `docs/YYYY/MM/DD/article-name.md`

Each article uses front matter with these fields:
- `title`: Article title
- `authors`: List of authors
- `date`: Publication date (YYYY/MM/DD)
- `file_name`: Associated PDF filename (optional)
- `linkedin`: LinkedIn post ID (optional)
- `youtube_id`: YouTube video ID (optional)
- `back_link`: Parent page link

### Adding New Content

1. For articles with PDFs, follow the workflow in `docs/admin/new-article-workflow.md`
2. PDFs must be added to the files submodule first
3. Use the provided macros for consistent formatting
4. Update relevant index pages (e.g., `docs/resources/presentations.md`)

### Version Management

The version is automatically incremented on each push and stored in the `version` file. The custom footer plugin reads this version for display.