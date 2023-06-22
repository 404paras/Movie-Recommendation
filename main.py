import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a3c77555c5a6e403ef573e8d48ac813c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_ind = movies[movies['title'] == movie].index[0]
    movie_poster=[]
    movie_list = sorted(enumerate(similarity[movie_ind]), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,movie_poster

similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_list)
st.title('Movie Recommandation System')
selected_movie = st.selectbox('Search Movie',
             movies['title'].values)

if st.button('Recommend'):

    name,poster = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])