from docling.document_converter import DocumentConverter
import sys


def run_docling(input_path, output_format="markdown"):
    """
    Run Docling on a document (PDF, DOCX, PPTX, XLSX, images, etc.).

    Docling converts documents into structured Markdown, HTML, or JSON
    with advanced PDF understanding including layout, reading order,
    table structure, code, formulas, and more.
    """
    try:
        converter = DocumentConverter()
        result = converter.convert(input_path)

        if output_format == "markdown":
            output = result.document.export_to_markdown()
        elif output_format == "html":
            output = result.document.export_to_html()
        elif output_format == "json":
            output = result.document.export_to_dict()
        else:
            output = result.document.export_to_markdown()

        print(f"--- Docling Result for {input_path} ---")
        print(output)
        print("-" * 40)

        return output
    except Exception as e:
        print(f"Error running Docling: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docling_ocr.py <input_path> [format: markdown|html|json]")
    else:
        output_format = sys.argv[2] if len(sys.argv) > 2 else "markdown"
        run_docling(sys.argv[1], output_format)
