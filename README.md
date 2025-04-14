<p align="center">
  <img src="https://github.com/user-attachments/assets/cb3b7cf9-52ea-4359-be0f-b70632ac6125" alt="Logo College" width="150">
</p>

# Shadow Project

**A classified, agent-aware RAG system for secure intelligence retrieval.**  
Built for high-stakes environments where information access must be precise, permissioned, and explainable.

---
![FlwoChart](https://github.com/user-attachments/assets/48a77ddb-2eda-4672-9190-236dc8c55256)

##  Project Overview

ShadowCircuit simulates a real-world classified intelligence assistant, designed to retrieve and justify sensitive information for agents operating at different clearance levels. Built on Retrieval-Augmented Generation (RAG), the system blends semantic search, rule-based logic, and dynamic prompt construction.

> “The right intel, to the right agent, at the right time — or not at all.”

---

![image](https://github.com/user-attachments/assets/4ebada81-313a-4f8d-85ec-2a47a46f4b3f)



## 🧱 Key Features

- 🔐 **Agent-Level Access Control**  
  Every query checks clearance before retrieval. No leaks. No exceptions.

- 🧠 **RAG-Powered Retrieval Pipeline**  
  Combines vector similarity and graph-based traversal for deep semantic matching.

- 📜 **Rule-Based Justification Engine**  
  Built-in response framework governs how answers are shaped per query type and agent level.

- 🗃️ **Modular Chunking Engine**  
  Custom chunker pre-processes documents for smart, targeted retrieval.

- 🌗 **Cryptic, Tactical, or Strategic Responses**  
  Answers adapt based on agent classification — from basic training to silent operations.

---

## 🧪 Example Use Case

```plaintext
Agent Level: 3
Query: How do I evade thermal surveillance while extracting a compromised asset?

Response:
Eyes open, Phantom. 🧠 Strategy Brief:
Use thermal decoys, mask signatures with industrial heat zones, and relocate through Phase-Shift Safehouses.
```

---

## 📂 Tech Stack

- `Streamlit` – Frontend for query submission  
- `sentence-transformers` – Embedding engine  
- `scikit-learn` – Similarity scoring  
- `LangChain`-ready architecture (extensible)  
- `python-docx`, `json`, `re` – Document processing

---

## 📦 Project Structure

```
project_shadow/
├── app.py                      # Streamlit frontend
├── data/                       # Source DOCX files
├── chunks/                     # Pre-processed semantic chunks
├── retrieval/                  # Vector + graph retrieval logic
├── rules/                      # Rule-matching response engine
├── utils/                      # Access control, prompt utils
├── scripts/                    # Chunk generation script
└── docs/                       # Technical explanation (optional)
```

---

## 🧠 Ideal For

- RAG prototyping with explainability
- Secure document question-answering
- LLM sandboxing with role-based control
- Intelligence or law-enforcement training sims

---

## ✅ Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Generate chunks:
```bash
python -m scripts.generate_chunks
```

3. Run the app:
```bash
streamlit run app.py --server.fileWatcherType none
```

---

## 🧠 Built With Purpose

This system was designed for [Project SHADOW], simulating covert data access inside a high-risk, zero-trust environment.  
Responses are customized, cryptic, or codified depending on the agent's clearance level and context.

> 🫥 Trust no one. Assume nothing. Adapt or be eliminated.
