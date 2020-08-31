# Import Python packages
import pandas as pd
import numpy as np
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

def get_data_spotify(user_input, lang_input):

    # Provide Authentication to access Spotify API
    client_id = 'e3769c0505454a7398b3b788361aaa9f'
    client_secret = '11494f7ea99b4e0eb7b66e1ccef1bd74'       #<----------------- YOUR SECRET HERE
    username = '11102482152'                                #<----------------- YOUR USERNAME HERE

    redirect_uri = 'https://developer.spotify.com/dashboard/applications/e3769c0505454a7398b3b788361aaa9f'
    token = util.prompt_for_user_token(username=username,
                                       #scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    #Setting user input as search string

    search = user_input

    #Setting the endpoint url
    endpoint_url = "https://api.spotify.com/v1/search?"

    # PERFORM THE QUERY
    id_list = []
    name_list = []                                         # create empty lists to hold data
    desc_list = []
    img_list = []
    url_list = []
    markets_list = []
    lang_list = []

    type = 'show'
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
            markets_list.append(json_response['shows']['items'][i]['available_markets'])
            lang_list.append(json_response['shows']['items'][i]['languages'])

        more_runs = (json_response['shows']['total'] // 50 )            # how many more runs of 50 are needed?

        counter += 1                                                    # increase conditional counter by 1

        offset = offset + 50


    #Build Dataframe with all podcasts
    podcasts = pd.DataFrame()

    podcasts['id'] = id_list
    podcasts['name'] = name_list
    podcasts['description'] = desc_list
    podcasts['images'] = img_list
    podcasts['url'] = url_list
    podcasts['markets'] = markets_list
    podcasts['languages'] = lang_list

    # List episodes for each podcast:
    # GET https://api.spotify.com/v1/shows/{id}/episodes

    # get a list of all show ids for later

    show_list = list(podcasts['id'])

    # PERFORM THE QUERY

    show_id_list = []                                       # create empty lists to hold data
    id_list = []
    dur_list = []
    date_list = []
    name_list = []
    desc_list = []
    img_list = []
    url_list = []
    lang_list = []

    for show_id in show_list:                               # iterate through every show in show_list

        more_runs = 1                                       # instantiate conditional variables
        counter = 0

        id = show_id                                        # assign variables for search query
        type = 'episodes'                                      # start the offset at 0
        limit = 50
        offset = 0
        languages = list(lang_input)

                                                                 # max offset is 2000 including limit
        while((offset <= 1950) & (counter <= more_runs)):        # while loop to run with conditional variables

            endpoint_url = f"https://api.spotify.com/v1/shows/{id}/episodes?"

            query = f'{endpoint_url}'
            query += f'&q={search}'                              # format the query with assigned variables
            query += f'&type={type}'
            query += f'&offset={offset}'
            query += f'&limit={limit}'
            query += f'&languages={languages}'

            response = requests.get(query,                                      # send a get request
                           headers={"Content-Type":"application/json",
                                    "Authorization":f"Bearer {token}"})
            json_response = response.json()                                     # get response as a json file


            offset = offset + 50                                     # increase the offset by 50
            counter += 1                                             # increase the counter by 1


            if next(iter(json_response)) != 'error':                 # if there wasn't any errors append data

                for i in range(len(json_response['items'])):                        # loop through json

                    show_id_list.append(show_id)
                    id_list.append(json_response['items'][i]['id'])                 # pull out info from json
                    dur_list.append(json_response['items'][i]['duration_ms'])       # append into empty lists
                    date_list.append(json_response['items'][i]['release_date'])
                    name_list.append(json_response['items'][i]['name'])
                    desc_list.append(json_response['items'][i]['description'])
                    url_list.append(json_response['items'][i]['external_urls']['spotify'])
                    lang_list.append(json_response['items'][i]['languages'])
                    img_list.append(json_response['items'][i]['images'][0]['url'])


                more_runs = (json_response['total'] // 50 )              # how many more runs of 50 are needed

    # setup a dataframe from the lists

    all_episodes = pd.DataFrame()

    all_episodes['show_id'] = show_id_list
    all_episodes['episode_id'] = id_list
    all_episodes['length(ms)'] = dur_list
    all_episodes['date'] = date_list
    all_episodes['episode_name'] = name_list
    all_episodes['description'] = desc_list
    all_episodes['url'] = url_list
    all_episodes['img'] = img_list
    all_episodes['languages'] = lang_list

    # create a dictionary of show ids and show names

    fmap = podcasts.groupby('id')['name'].apply(list).to_dict()

    # map dictionary to show id in dataframe

    all_episodes['show_name'] = all_episodes['show_id'].map(fmap)

    # remove the brackets [] from each show name

    all_episodes['show_name'] = all_episodes['show_name'].str[0]

    all_episodes['length(min)'] = all_episodes['length(ms)'] / 60000

    all_episodes = all_episodes[all_episodes['length(min)'] > 5.0]

    all_episodes['title_and_description'] = all_episodes['episode_name'] + ' ' + all_episodes['description']

    return all_episodes
