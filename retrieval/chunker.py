# Logic to chunk .docx documents into usable text blocks
from typing import List
import re


def split_text(text: str, max_length: int = 500) -> List[str]:
    """
    Simple chunking based on sentence boundaries. You can customize with sliding windows or overlapping chunks.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
