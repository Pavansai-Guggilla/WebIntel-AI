# WebIntel-AI
WebIntel AI is an intelligent web scraper that extracts data, filters key content, and summarizes it using AI. It automates web scraping, keyword extraction, and RAG-based search, making it ideal for researchers and analysts who need quick insights from large amounts of text.



# 🌍 **WebIntel AI** – Smart Web Scraping, Summarization & RAG Search 🧠📊  

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![ML](https://img.shields.io/badge/MachineLearning-NLP-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)  

## 🌟 **Project Overview**  
**WebIntel AI** is an **intelligent web scraper and AI-powered text processor** that transforms raw website content into meaningful insights using **NLP-driven summarization and keyword extraction**. This tool helps researchers, analysts, and businesses to **automate content extraction**, **filter key information**, and **build AI-driven search engines** for better knowledge discovery.  

---

## 🏆 **Why WebIntel AI?**  
We live in an era of **data overload** 📈. Manually browsing, reading, and extracting useful information is **time-consuming** and **inefficient**. **WebIntel AI** solves this by:  

✅ **Automatically Scraping** data from the web 🌐  
✅ **Filtering Relevant Content** based on keywords 🔍  
✅ **Summarizing Key Insights** using AI 🤖  
✅ **Building a Smart Search Index** for instant retrieval 📚  

This tool is perfect for **journalists, researchers, market analysts, and AI enthusiasts** looking for **automated, AI-powered knowledge extraction**. 📊  

---

## 🚀 **How WebIntel AI Works?**  

1️⃣ **Smart Web Scraping** 🕷️  
   - **Extracts links & content** from websites  
   - Uses **`BeautifulSoup`** for structured parsing  
   - Stores data in **clean JSON format**  

2️⃣ **AI-Powered Text Processing** 🧠  
   - Summarization with **`BART Transformer`**  
   - Keyword Extraction using **`TF-IDF`**  
   - **RAG-based AI search** for quick lookup  

3️⃣ **Optimized Performance** ⚙️  
   - **Caching system** for efficiency  
   - **Configurable delays** to avoid IP bans  
   - **Parallel processing** for speed  

---

## 📁 **Project Structure**  

```
📂 WebIntel-AI
│── 📜 main.py              # Pipeline runner
│── 📜 config.py            # Configuration settings
│── 📂 scraper
│   ├── 📜 scraper.py       # Web Scraper
│   ├── 📜 link_extractor.py # Extracts URLs
│   ├── 📜 request_handler.py # Handles HTTP requests
│── 📂 ml
│   ├── 📜 ml_summarizer.py  # AI Summarization
│   ├── 📜 ml_ai_processor.py # Keyword Extraction
│   ├── 📜 rag_model.py      # RAG-based AI search
│── 📂 cache
│   ├── 📜 cache.py         # Caching system
│── 📂 data                 # Stores extracted data
```

---

## 📌 **Setup & Installation**  

### 🔧 **Requirements**
Make sure you have Python **3.8+** installed.  

#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/WebIntel-AI.git
cd WebIntel-AI
```

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Pipeline  
```bash
python main.py "https://example.com" --keywords "AI, Machine Learning" --prompt "Summarize this article:"
```

---

## ⚙️ **Configuration Options**  

Modify `config.py` to **adjust scraper behavior**:  

```python
SCRAPER_DELAY_MIN = 5   # Min delay in seconds  
SCRAPER_DELAY_MAX = 15  # Max delay in seconds  
CACHE_DIR = "cache"     # Cache location  
DATA_DIR = "data"       # Extracted JSON storage  
```

---

## 💡 **Key Technologies Used**  

| Feature                | Library Used 📦 |
|------------------------|----------------|
| Web Scraping          | `BeautifulSoup`, `requests` |
| AI Summarization      | `Transformers (BART)` |
| Keyword Extraction    | `TF-IDF` |
| RAG Search Engine    | `SentenceTransformers`, `FAISS` |
| Caching System       | `diskcache` |
| Parallel Processing  | `asyncio` (Optional) |

---



## 📜 **License**  
This project is licensed under **MIT License**.  

---

🔗 **WebIntel AI** is your **go-to solution** for AI-powered content extraction & knowledge discovery! 🚀 Try it out today! 🎯
