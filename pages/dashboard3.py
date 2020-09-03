import streamlit as st
from modules.recommender import recommendation_system_labeled
import pandas as pd
# pylint: disable=line-too-long


def get_data():
    data_labeled_spot = pd.read_csv('data/data_spotify_50_cluster_labeled.csv')
    data_labeled_yt = pd.read_csv('data/data_youtube_25_cluster_labeled.csv')
    data_labeled_medium = pd.read_csv('data/data_medium_10_cluster_labeled.csv')
    data_labeled_arxiv = pd.read_csv('data/data_arxiv_50_cluster_labeled.csv')
    data = [data_labeled_spot, data_labeled_yt, data_labeled_medium, data_labeled_arxiv]
    return data

data = get_data()

def write():
    """Used to write the page in the app.py file"""
    #with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")

    #st.write()


    page_bg_img = '''
                  <style>
                  body {
                  background-image: url("https://images.unsplash.com/photo-1474390690775-517486716e55?ixlib=rb-1.2.1&auto=format&fit=crop&w=1955&q=80");
                  background-size: cover;
                    }
                  </style>
                  '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title('philoML - The key to knowledge')

    user_input3 = st.text_input("Topic (please enter up to two keywords)", 'Data Science', key = '4')

    #user_input = input.lower().replace(' ','_')

    data_spot = recommendation_system_labeled(user_input3, data[0])
    data_yt = recommendation_system_labeled(user_input3, data[1])
    data_medium = recommendation_system_labeled(user_input3, data[2])
    data_arxiv = recommendation_system_labeled(user_input3, data[3])

    img_spotify = list(data_spot['img'][0:5])
    url_spotify = list(data_spot['url'][0:5])
    title_spotify = list(data_spot['episode_name'][0:5])

    img_yt = list(data_yt['images'][0:5])
    url_yt = list(data_yt['url'][0:5])
    title_yt = list(data_yt['name'][0:5])

    url_medium = list(data_medium['url'][0:5])
    title_medium = list(data_medium['title'][0:5])

    url_arxiv = list(data_arxiv['url'][0:5])
    title_arxiv = list(data_arxiv['title'][0:5])


    st.components.v1.html(f'<div class="row">\
                          <div class="column">\
                          <a target="_blank" rel="noopener noreferrer"\
                          href="https://medium.com"><img src="https://miro.medium.com/fit/c/256/256/1*6_fgYnisCa9V21mymySIvA.png" width="100" height="100"\
                          style="vertical-align:middle;margin:3px 3px;border-radius:50%;"></a>\
                          <a target="_blank" rel="noopener noreferrer"\
                          href={url_medium[0]}><img src="https://miro.medium.com/fit/c/256/256/1*6_fgYnisCa9V21mymySIvA.png" width="100" height="100"\
                          style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                          <a target="_blank" rel="noopener noreferrer"\
                          href={url_medium[1]}><img src="https://miro.medium.com/fit/c/256/256/1*6_fgYnisCa9V21mymySIvA.png"  width="100" height="100"\
                          title="test" style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                          <a target="_blank" rel="noopener noreferrer"\
                           href="https://arxiv.org"><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                          style="vertical-align:middle;margin:3px 3px;border-radius:50%;padding-left:2px"></a>\
                          <a target="_blank" rel="noopener noreferrer"\
                           href={url_arxiv[0]}><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                          title="{title_arxiv[0]}"" style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                          <a target="_blank" rel="noopener noreferrer"\
                           href={url_arxiv[1]}><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                          title="{title_arxiv[1]}"" style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                          </div>\
                          </div>', height=250)
