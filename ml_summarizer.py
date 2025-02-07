# ml/summarizer.py
from transformers import pipeline
import logging

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("✅ Summarizer model loaded!")
except Exception as e:
    print(f"❌ Error loading summarizer: {e}")
    summarizer = None

def summarize_text(text, prompt=None):
    """Summarize extracted text if it's long enough."""
    if not summarizer or len(text.split()) < 50:
        return text
    try:
        input_text = f"{prompt}\n\n{text}" if prompt else text
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)[0].get("summary_text", "")
        return summary
    except Exception as e:
        print(f"❌ Summarization error: {e}")
        return text
