import re

def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
    - Removing extra whitespace
    - Removing repeated newlines
    """
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
