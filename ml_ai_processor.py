# ml/ai_processor.py
import json
import logging
from sklearn.feature_extraction.text import TfidfVectorizer

def process_text(json_file):
    """Extract keywords using TF-IDF from a JSON file."""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        text = data.get("content", "")
        if not text:
            logging.warning(f"No content found in {json_file}")
            return []

        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform([text])
        keywords = vectorizer.get_feature_names_out()
        logging.info(f"Keywords extracted: {keywords[:10]}")
        
        return keywords.tolist()
    except Exception as e:
        logging.error(f"Error processing {json_file}: {e}")
        return []
