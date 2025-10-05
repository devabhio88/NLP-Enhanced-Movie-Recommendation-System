# NLP-Enhanced-Movie-Recommendation-System
A content-based movie recommender built using Python, Pandas, NumPy, and Scikit-learn, enhanced with NLP preprocessing (Stemming). This project analyzes metadata such as movie overviews, genres, cast, crew, and keywords from the TMDB 5000 Movies dataset to recommend top-5 similar films based on textual similarity.

# 🎬 NLP-Enhanced Movie Recommendation System

A **content-based movie recommender** built using **Python**, **Scikit-learn**, and **Streamlit**, enhanced with **Natural Language Processing (NLP)** techniques like stemming and text vectorization.  
The system analyzes movie metadata — such as overview, genres, cast, crew, and keywords — to recommend **top-5 similar movies** based on content similarity.

---

## 🧠 Project Overview

With thousands of movies available, users often struggle to find films similar to their favorites.  
This project aims to solve that problem using **content-based filtering** and **NLP preprocessing**, providing intelligent movie recommendations through an interactive web interface.

---

## 🚀 Features

- 🔍 **Content-Based Recommendation Model** — Suggests similar movies using cosine similarity between vectorized metadata.  
- 🧩 **NLP Preprocessing** — Includes stemming and token normalization for accurate similarity matching.  
- 📊 **Data Cleaning & Feature Engineering** — Extracts and merges genres, keywords, cast, and crew information from TMDB datasets.  
- 🌐 **Streamlit Web App** — User-friendly UI for selecting movies and viewing recommendations in real time.  
- 🎞️ **TMDB API Integration** — Fetches movie posters dynamically to enhance the visual experience.  
- 💾 **Model Serialization** — Uses Pickle to store preprocessed data and similarity matrices for faster deployment.

---

## 🧩 Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Programming Language** | Python |
| **Libraries** | NumPy, Pandas, Scikit-learn, NLTK |
| **Web Framework** | Streamlit |
| **API** | TMDB (The Movie Database) API |
| **Serialization** | Pickle |

---

## 📊 Workflow

### 1️⃣ Data Collection  
- Used TMDB 5000 Movies and Credits datasets.  
- Merged them using common titles.  

### 2️⃣ Data Preprocessing  
- Removed null and duplicate entries.  
- Parsed JSON-like fields using `ast.literal_eval`.

### 3️⃣ Feature Engineering  
- Extracted and combined important attributes: `overview`, `genres`, `cast`, `crew`, and `keywords`.  
- Applied stemming to normalize text and created a combined `tags` column.  

### 4️⃣ Model Building  
- Used `CountVectorizer(max_features=5000, stop_words='english')` to build a Bag-of-Words model.  
- Computed **cosine similarity** between movie vectors to determine closeness.  

### 5️⃣ Deployment  
- Built an interactive **Streamlit app** to input a movie and display top-5 similar titles with posters fetched from the **TMDB API**.  

---

## 🧰 Installation & Usage

### 📦 Clone the Repository
```bash
git clone https://github.com/devabhio88/NLP-Enhanced-Movie-Recommender.git
cd NLP-Enhanced-Movie-Recommender
