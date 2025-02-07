# ml/rag_model.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import logging

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    logging.error(f"Error loading SentenceTransformer: {e}")
    model = None

def embed_text(text):
    """Generate an embedding for text."""
    return model.encode(text) if model else None

def build_rag_index(text_list):
    """Build a FAISS index from a list of texts."""
    if not model or not text_list:
        return None

    embeddings = np.array([embed_text(text) for text in text_list if text]).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index
