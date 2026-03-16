import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Movie Recommender", layout="wide")

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
background-color:#0e1117;
color:white;
}

.movie-card {
background-color:#1c1f26;
padding:20px;
border-radius:12px;
text-align:center;
font-size:18px;
font-weight:bold;
}

.movie-card:hover{
transform:scale(1.05);
transition:0.3s;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO IMAGE ----------------
st.image(
    "C:\\Users\\ANAND\\Desktop\\Machine-learning-projects\\movie-recommandation\\hero.png",

)

st.title("🎬 AI Movie Recommendation System")
st.write("Find movies similar to the one you love.")

selected_movie = st.selectbox(
    "Search your favorite movie",
    movies['title'].values
)

# ---------------- RECOMMEND BUTTON
if st.button("Recommend 🍿"):

    with st.spinner("Finding the best movies for you... 🍿"):

        names = recommend(selected_movie)

        cols = st.columns(len(names))

        for i in range(len(names)):
            with cols[i]:
                st.markdown(f"""
                <div class="movie-card">
                    {names[i]}
                </div>
                """, unsafe_allow_html=True)