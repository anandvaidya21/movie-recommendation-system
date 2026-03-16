# 🎬 AI Movie Recommendation System

An AI-powered **Movie Recommendation System** built using **Machine Learning and Streamlit** that suggests movies similar to the one selected by the user.
The system uses **content-based filtering** and **cosine similarity** to recommend movies based on features such as genres, keywords, cast, and overview.

---

## 🚀 Live Demo

🔗 https://movie-recommendation-system-by-anand.streamlit.app

---

## 📌 Features

* 🎥 Recommend movies based on user selection
* 🤖 Content-based recommendation using **Machine Learning**
* ⚡ Fast similarity computation using **cosine similarity**
* 🎨 Clean and interactive **Streamlit UI**
* 🌙 Dark themed interface for better user experience

---

## 🧠 How It Works

1. Movie metadata is processed and combined into a **tags feature**.
2. The **CountVectorizer** converts text features into numerical vectors.
3. **Cosine Similarity** measures similarity between movies.
4. When a user selects a movie, the system returns the **top 5 most similar movies**.

---

## 🛠 Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**

---

## 📂 Project Structure

```
movie-recommendation-system
│
├── app.py
├── movie_dict.pkl
├── hero.png
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ Run Locally

Clone the repository

```
git clone https://github.com/anandvaidya21/movie-recommendation-system.git
```

Go to the project directory

```
cd movie-recommendation-system
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit app

```
streamlit run app.py
```

---




---

## 👨‍💻 Author

**Anand Vaidya**

* AIML Student
* Full Stack Developer
* Machine Learning Enthusiast
* Gen ai & LLM Enthusiast

GitHub: https://github.com/anandvaidya21

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
