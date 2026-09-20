# Zerox OCR

Zerox by OmniAI is a dead-simple way to OCR documents for AI ingestion. It converts files (PDF, DOCX, images) into images and passes them to vision models (GPT-4o, Claude, Gemini, etc.) to extract structured Markdown.

## Prerequisites

- **Poppler** must be installed and available in your system PATH (required for PDF processing).
- Set the appropriate API key for your chosen vision model provider:
  - OpenAI: `OPENAI_API_KEY`
  - Anthropic: `ANTHROPIC_API_KEY`
  - Google Gemini: `GEMINI_API_KEY`
  - Azure OpenAI: `AZURE_API_KEY`, `AZURE_API_BASE`, `AZURE_API_VERSION`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python zerox_ocr.py <file_path> [model]
```

### Examples

```bash
# Using OpenAI GPT-4o-mini (default)
python zerox_ocr.py ../tests/medium/table_1.png

# Using Claude
python zerox_ocr.py ../tests/medium/table_1.png claude-3-opus-20240229
```
