import os
import json
from docx import Document
from retrieval.chunker import split_text

def read_docx(path):
    doc = Document(path)
    return "\n".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])

def save_chunks(text, out_path, source_label):
    chunks = split_text(text, max_length=500)
    chunk_data = [{"id": f"{source_label}_{i}", "text": c} for i, c in enumerate(chunks)]

    with open(out_path, "w") as f:
        json.dump(chunk_data, f, indent=2)
    print(f"✅ Saved {len(chunk_data)} chunks to {out_path}")

if __name__ == "__main__":
    os.makedirs("chunks", exist_ok=True)

    manuals = [
        {
            "path": "data/secret_info_manual.docx",
            "out": "chunks/secret_info_chunks.json",
            "label": "secret"
        },
        {
            "path": "data/rag_case_response_framework.docx",
            "out": "chunks/response_framework_chunks.json",
            "label": "rules"
        }
    ]

    for manual in manuals:
        print(f"📖 Processing {manual['path']}")
        text = read_docx(manual["path"])
        save_chunks(text, manual["out"], manual["label"])
