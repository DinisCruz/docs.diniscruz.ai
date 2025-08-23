# LLM Brief: Creating Monthly Research Publication Index Pages

## Objective
In an artifact page, create a comprehensive monthly index page for research documents published by Dinis Cruz (from https://docs.diniscruz.com) during a specific month in 2025.

## Input Requirements
1. A folder structure showing the research documents for a specific month
2. The markdown files should follow the pattern: `YYYY/MM/DD/title-of-document.md`
3. Each document typically contains:
   - Title
   - Authors (usually "Dinis Cruz" and "ChatGPT Deep Research")
   - Date
   - PDF file reference
   - Back link (indicating the research category/area)
   - Content with abstract or executive summary

## Output Structure

### 1. File Name
The output file should be named: `YYYY-month.md` (e.g., `2025-june.md`, `2025-august.md`)
Located at the root of the month folder (e.g., `/06/2025-june.md`)

### 2. Page Title
Format: `[Month] [Year] Published Materials` (e.g., "June 2025 Published Materials")

### 3. Introduction Paragraph
Write two paragraph that includes:
- Total count of research documents published
- Breakdown by main areas/topics with counts
- Key themes and focus areas that emerge across the publications
- Any notable patterns or emphases in that month's research

### 4. Overview Table
Create a table with the following columns:
- **Date**: Format as MM/DD (e.g., 06/15)
- **Title**: Linked to the document using relative paths from the month root
- **Focus Area**: Extract from the back_link field or infer from content
- **Key Concepts**: 3-5 main concepts from the document

### 5. Detailed Summaries
For each document, provide:
- **Heading**: Document title followed by the date in italics
- **Two paragraphs**:
  - First paragraph: Core concepts, approach, and main contributions
  - Second paragraph: Technical details, implementation aspects, or practical applications
- Include links to the document when first mentioning it in each summary

## Formatting Guidelines

### Links
- All document links should be relative from the month root folder
- Format: `DD/document-title.md` (e.g., `15/semantic-knowledge-graphs-analysis.md`)
- Include links in both the table and when first mentioning documents in summaries

### Key Concepts
Extract the most important technical concepts, methodologies, or frameworks mentioned, such as:
- Specific technologies (e.g., MGraph-DB, Memory_FS)
- Architectural patterns (e.g., serverless, LETS pipeline)
- Methodologies (e.g., semantic knowledge graphs, G³)
- Standards or regulations (e.g., GDPR, ESG)

## Style Guidelines

1. **Professional Tone**: Write in a clear, technical style appropriate for a professional audience
2. **Comprehensive Coverage**: Ensure all documents are included and properly summarized
3. **Highlight Connections**: Where documents relate to each other or build on similar concepts, note these connections
4. **Avoid Redundancy**: While being comprehensive, avoid repeating the same information unnecessarily
5. **Emphasize Innovation**: Highlight novel approaches, frameworks, or solutions presented in the research

## Example Summary Structure

```markdown
### [Document Title]
*[Month Day], [Year]*

This [type of document] presents/explores/introduces [main topic/innovation] that [primary value proposition or problem it solves]. The [paper/brief/analysis] [key action: demonstrates/outlines/examines] how [main approach or methodology] can [primary benefit or outcome]. [Additional context about scope, methodology, or unique aspects].

The [implementation/analysis/framework] [specific technical details or components]. [Description of architecture, workflow, or technical approach]. [Key results, benefits, or implications]. The [document/research] [concluding point about significance, future applications, or relationship to broader field].
```

## Quality Checks
Before finalizing, ensure:
- All documents in the folder are included
- All links work correctly (relative paths from month root)
- The introduction accurately reflects the content distribution
- Each summary captures the essence of the document
- Technical terms are used accurately
- The page provides value both as a standalone overview and as input for further LLM processing