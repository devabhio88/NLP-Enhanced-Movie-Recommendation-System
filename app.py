# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import time
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c13146c724f3a92b3505a9ea6b4ae0ff&language=en-US'.format(movie_id))
#     data = response.json()
#     return "http://image.tmdb.org/t/p/w500/"+data['poster_path']
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         #fetch poster from API
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#         time.sleep(0.05)
#     return recommended_movies,recommended_movies_posters
#
# # fxn ends ####################################################
#
# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl','rb'))
# st.title('Movie Recommendation System')
#
# selected_movie_name = st.selectbox(
#     'What will like to watch',movies['title'].values
# )
#
# if st.button('Recommend'):
#     name,posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#         st.text(name[0])
#         st.image(posters[0])
#
#     with col2:
#         st.text(name[1])
#         st.image(posters[1])
#
#     with col3:
#         st.text(name[2])
#         st.image(posters[2])
#
#     with col4:
#         st.text(name[3])
#         st.image(posters[3])
#
#     with col5:
#         st.text(name[4])
#         st.image(posters[4])
#
#
import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- Create a robust Session object for all API calls ---
# This is the key change to solve the connection error.

session = requests.Session()
retry = Retry(
    total=5,  # Total number of retries
    backoff_factor=0.5,  # A delay factor between retries: {backoff factor} * (2 ** ({number of total retries} - 1))
    status_forcelist=[500, 502, 503, 504]  # Retry on these server error codes
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


# -----------------------------------------------------------

def fetch_poster(movie_id):
    """
    Fetches a movie poster using the robust session object.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c13146c724f3a92b3505a9ea6b4ae0ff&language=en-US"
    try:
        # Use session.get() instead of requests.get()
        response = session.get(url)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"

    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")  # Show the error in the app for debugging
        return "https://via.placeholder.com/500x750.png?text=API+Error"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# --- App Layout ---

st.title('🎬 Movie Recommendation System')

# Load data
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Data files not found. Make sure 'movie_dict.pkl' and 'similarity.pkl' are in the directory.")
    st.stop()

selected_movie_name = st.selectbox(
    'What would you like to watch?',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Finding recommendations...'):
        names, posters = recommend(selected_movie_name)

        if names:  # Check if recommendations were returned
            col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
            with col1:
                st.text(names[0])
                st.image(posters[0])
            with col2:
                st.text(names[1])
                st.image(posters[1])
            with col3:
                st.text(names[2])
                st.image(posters[2])
            with col4:
                st.text(names[3])
                st.image(posters[3])
            with col5:
                st.text(names[4])
                st.image(posters[4])