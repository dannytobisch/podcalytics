"""Home page shown when the user enters the application"""
import numpy as np

import streamlit as st

import pandas as pd
import numpy as np

import json
import requests
import urllib.parse

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

import matplotlib.pyplot as plt
import seaborn as sns

import datetime

from bokeh.models.widgets import Div

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")
        st.write()




    @st.cache
    def get_data(search):

        client_id = 'e3769c0505454a7398b3b788361aaa9f'

        client_secret = '11494f7ea99b4e0eb7b66e1ccef1bd74'       #<----------------- YOUR SECRET HERE

        username = '11102482152'                                #<----------------- YOUR USERNAME HERE

        #scope = 'playlist-modify-public playlist-modify'

        redirect_uri = 'https://developer.spotify.com/dashboard/applications/e3769c0505454a7398b3b788361aaa9f'

        token = util.prompt_for_user_token(username=username,
                                           #scope=scope,
                                           client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirect_uri)

        endpoint_url = "https://api.spotify.com/v1/search?"



        # PERFORM THE QUERY

        id_list = []
        name_list = []                                         # create empty lists to hold data
        desc_list = []
        img_list = []
        url_list = []

        type = 'show'
        market  = 'US'
        limit = 50                                             # assign variables for search query
        offset = 0                                             # start offset at 0


        more_runs = 1                                          # instantiate conditional variables
        counter = 0

                                                                    # max offset is 2000 including limit
        while((offset <= 1950) & (counter <= more_runs)):           # while loop to run with conditional variables



            query = f'{endpoint_url}'
            query += f'&q={search}'
            query += f'&type={type}'
            query += f'&offset={offset}'                       # format search query with assigned variables
            query += f'&market={market}'
            query += f'&limit={limit}'


            response = requests.get(query,                                           # get request
                           headers={"Content-Type":"application/json",
                                    "Authorization":f"Bearer {token}"})
            json_response = response.json()                                           # as a json file


            for i in range(len(json_response['shows']['items'])):                      # loop through json

                id_list.append(json_response['shows']['items'][i]['id'])               # pull out info from json
                name_list.append(json_response['shows']['items'][i]['name'])           # into empty lists
                desc_list.append(json_response['shows']['items'][i]['description'])
                img_list.append(json_response['shows']['items'][i]['images'][0]['url'])
                url_list.append(json_response['shows']['items'][i]['external_urls']['spotify'])

            more_runs = (json_response['shows']['total'] // 50 )            # how many more runs of 50 are needed?

            counter += 1                                                    # increase conditional counter by 1

            offset = offset + 50



        podcasts = pd.DataFrame()

        podcasts['id'] = id_list
        podcasts['name'] = name_list
        podcasts['description'] = desc_list
        podcasts['images'] = img_list
        podcasts['url'] = url_list

        return podcasts

    user_input = st.text_input("Topic", 'data science')

    podcasts = get_data(user_input)

    imgs = list(podcasts['images'][0:22])
    url = list(podcasts['url'][0:22])

    st.components.v1.html(f'<div class="row">\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                  href="https://spotify.com"><img src="https://lh3.googleusercontent.com/UrY7BAZ-XfXGpfkeWg0zCCeo-7ras4DCoRalC_WXXWTK9q5b0Iw7B0YQMsVxZaNB7DM=s360-rw" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                  href={url[1]}><img src={imgs[1]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%""></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[2]}><img src={imgs[2]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%""></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                    href="https://youtube.com"><img src="https://stagewp.sharethis.com/wp-content/uploads/2018/02/youtube.png" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[4]}><img src="https://i.ytimg.com/vi/xC-c7E5PK0Y/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[5]}><img src="https://i.ytimg.com/vi/X3paOmcrTjQ/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[6]}><img src={imgs[6]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[0]}><img src={imgs[0]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[8]}><img src={imgs[8]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[9]}><img src="https://i.ytimg.com/vi/4OZip0cgOho/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                 <a target="_blank" rel="noopener noreferrer"\
                  href={url[10]}><img src="https://i.ytimg.com/vi/ua-CiDNNj30/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[11]}><img src="https://i.ytimg.com/vi/Ck0ozfJV9-g/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  </div>', height=250)

    st.components.v1.html(f'<div class="row">\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                  href="https://medium.com"><img src="https://miro.medium.com/fit/c/256/256/1*6_fgYnisCa9V21mymySIvA.png" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:50%;"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                  href={url[12]}><img src={imgs[12]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[13]}><img src={imgs[13]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href="https://arxiv.org"><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:50%;padding-left:2px"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[14]}><img src={imgs[14]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[15]}><img src={imgs[15]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[16]}><img src={imgs[16]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[17]}><img src={imgs[17]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[18]}><img src={imgs[18]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[19]}><img src={imgs[19]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                 <a target="_blank" rel="noopener noreferrer"\
                  href={url[20]}><img src={imgs[20]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[21]}><img src={imgs[21]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  </div>', height=250)
