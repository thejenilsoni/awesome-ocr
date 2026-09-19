# Awesome OCR: A Comprehensive Collection of OCR Libraries and Models

This repository serves as a comprehensive collection of code examples and test documents for various Optical Character Recognition (OCR) libraries and State-of-the-Art (SOTA) models. The goal is to provide a practical resource for developers and researchers to compare the performance of different OCR solutions across a range of document complexities, from simple digital text to complex, handwritten, and multi-column layouts.

## Table of Contents
1. [OCR Landscape: Traditional vs. SOTA](#ocr-landscape-traditional-vs-sota)
2. [Repository Structure](#repository-structure)
3. [Test Documents](#test-documents)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)

## OCR Landscape: Traditional vs. SOTA

The field of OCR has evolved significantly, moving from rule-based systems to deep learning models, and now to powerful Vision-Language Models (VLMs) based on the Transformer architecture.

## Repository Structure

The repository currently contains a focused initial release with these OCR modules:

- `tesseract/` — classic Tesseract OCR engine with example scripts and configuration.
- `easyocr/` — lightweight PyTorch-based OCR for simple and multilingual text extraction.
- `paddleocr/` — PaddlePaddle OCR with layout-aware detection and strong multilingual support.
- `marker/` — fast, high-accuracy PDF to Markdown conversion with advanced document understanding.
- `surya/` — transformer-based OCR with strong layout analysis and high accuracy on complex documents.
- `doctr/` — deep-learning OCR examples using docTR (PyTorch/TensorFlow) for end-to-end recognition.
- `rapidocr/` — lightweight, high-speed OCR optimized for edge and low-latency applications.
- `docling/` — IBM's document processing toolkit for converting PDFs and other formats to Markdown, HTML, or JSON.
- `nougat/` — Meta AI's model for transcribing scientific PDFs while preserving LaTeX mathematics and tables.

Each module folder includes a model-specific script, a `requirements.txt`, and a module README explaining how to run that example.

`README-FULL.md` contains the complete project roadmap and the full list of planned OCR libraries and models.

## Test Documents

The repository includes a `tests/` folder organized by difficulty:

- `tests/simple/` — clean digital text and simple scanned pages.
- `tests/medium/` — documents with tables, mixed layouts, or moderate noise.
- `tests/hard/` — low-resolution scans, handwriting, and complex multi-column pages.

These test categories help validate OCR performance across a range of real-world scenarios.

## Setup and Installation

### Prerequisites

- Python 3.8 or newer
- Git
- For `tesseract/`, install the `tesseract-ocr` engine on your system

### Install dependencies

Install dependencies for a specific module by changing into its folder and using pip:

```bash
cd tesseract
pip install -r requirements.txt
```

Repeat for `easyocr/` and `paddleocr/` when needed.

## Usage

Run one of the example OCR scripts with a test image or document path:

```bash
cd easyocr
python easyocr_ocr.py ../tests/medium/sample.png
```

For a Tesseract example:

```bash
cd tesseract
python tesseract_ocr.py ../tests/simple/sample.png
```

For PaddleOCR:

```bash
cd paddleocr
python paddleocr_ocr.py ../tests/medium/sample.png
```

As this project grows, more modules and usage examples will be added from `README-FULL.md`.