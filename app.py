import pickle

import pandas as pd
import requests
import streamlit as st


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_moviePosters = []
    for i in movies_list:
            movie_id=movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_moviePosters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_moviePosters
def fetch_poster(movie):

    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7638e7f823f32eb51737cc434f6a5559'.format(movie))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']
st.title('Movie Recommender System')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
selected_movie_name= st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.subheader(names[0])
        st.image(posters[0])
    with col2:
        st.subheader(names[1])
        st.image(posters[1])
    with col3:
        st.subheader(names[2])
        st.image(posters[2])
    with col4:
        st.subheader(names[3])
        st.image(posters[3])
    with col5:
        st.subheader(names[4])
        st.image(posters[4])

# st.write('You selected:', option)