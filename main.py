import pickle
import streamlit as st
import requests
import os
os.chdir(r'C:\Users\monik\PycharmProjects\movie_recommendation')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2= st.columns(2)
    with col1:
        st.write(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],width=250)
    with col2:
        st.write(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],width=250)
    with col1:
        st.write(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],width=250)
    with col2:
        st.write(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],width=250)
    with col1:
        st.write(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],width=250)
    with col2:
        st.write(recommended_movie_names[5])
        st.image(recommended_movie_posters[5],width=250)

