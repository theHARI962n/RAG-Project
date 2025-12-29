from typing import List
from app.utils.text_cleaner import clean_text

def chunk_pages(
    pages: List[dict],
    chunk_size: int = 500,
    overlap: int = 100
):
    """
    Input:
    [
      {"page": 1, "text": "..."},
      {"page": 2, "text": "..."}
    ]

    Output:
    [
      {
        "text": "chunk text",
        "metadata": {
          "page": 1
        }
      }
    ]
    """
    chunks = []

    for page in pages:
        cleaned_text = clean_text(page["text"])
        words = cleaned_text.split()

        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            chunks.append({
                "text": chunk_text,
                "metadata": {
                    "page": page["page"]
                }
            })

            start = end - overlap

    return chunks
