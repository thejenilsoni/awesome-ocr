import asyncio
import os
import sys

from pyzerox import zerox


async def run_zerox(file_path, model="gpt-4o-mini"):
    """
    Run Zerox OCR on a document (PDF, DOCX, image, etc.).

    Zerox converts documents into Markdown using vision models
    (GPT-4o, Claude, Gemini, etc.). Requires appropriate API keys
    set as environment variables.
    """
    try:
        result = await zerox(
            file_path=file_path,
            model=model,
            cleanup=True,
            concurrency=10,
            maintain_format=False,
        )

        print(f"--- Zerox OCR Result for {file_path} ---")
        print(result)
        print("-" * 40)

        return result
    except Exception as e:
        print(f"Error running Zerox: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python zerox_ocr.py <file_path> [model]")
        print("  Supported models: gpt-4o-mini (default), gpt-4o, claude-3-opus-20240229, etc.")
        print("  Set required API keys as environment variables (e.g., OPENAI_API_KEY)")
    else:
        file_path = sys.argv[1]
        model = sys.argv[2] if len(sys.argv) > 2 else "gpt-4o-mini"
        asyncio.run(run_zerox(file_path, model))
