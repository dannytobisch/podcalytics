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
    st.title('Dashboard')


    user_input = st.text_input("Topic (please enter up to three keywords)", 'Data Science')

    data_spot = recommendation_system_labeled(user_input, data[0])
    data_yt = recommendation_system_labeled(user_input, data[1])
    data_medium = recommendation_system_labeled(user_input, data[2])
    data_arxiv = recommendation_system_labeled(user_input, data[3])

    img_spotify = list(data_spot['img'][0:5])
    url_spotify = list(data_spot['url'][0:5])

    img_yt = list(data_yt['images'][0:5])
    url_yt = list(data_yt['url'][0:5])

    url_medium = list(data_medium['url'][0:5])

    url_arxiv = list(data_arxiv['url'][0:5])

    st.components.v1.html(f'<div class="row">\
                      <div class="column">\
                      <a target="_blank" rel="noopener noreferrer"\
                      href="https://spotify.com"><img src="https://lh3.googleusercontent.com/UrY7BAZ-XfXGpfkeWg0zCCeo-7ras4DCoRalC_WXXWTK9q5b0Iw7B0YQMsVxZaNB7DM=s360-rw" width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                      href={url_spotify[0]}><img src={img_spotify[0]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%""></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_spotify[1]}><img src={img_spotify[1]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%""></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                        href="https://youtube.com"><img src="https://stagewp.sharethis.com/wp-content/uploads/2018/02/youtube.png" width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_yt[0]}><img src={img_yt[0]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_yt[1]}><img src={img_yt[1]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      </div>\
                      <div class="column">\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_spotify[2]}><img src={img_spotify[2]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_spotify[3]}><img src={img_spotify[3]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_spotify[4]}><img src={img_spotify[4]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_yt[2]}><img src={img_yt[2]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                     <a target="_blank" rel="noopener noreferrer"\
                      href={url_yt[3]}><img src={img_yt[3]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_yt[4]}><img src={img_yt[4]} width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      </div>\
                      </div>', height=250)

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
                      style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href="https://arxiv.org"><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:50%;padding-left:2px"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_arxiv[0]}><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      <a target="_blank" rel="noopener noreferrer"\
                       href={url_arxiv[1]}><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                      style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                      </div>\
                      </div>', height=250)


