import streamlit as st
import pandas as pd
import numpy as np
from pages.dashboard import get_data
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D

# matplotlib.style.use('ggplot')
model = Word2Vec.load("model/model_w2v.model")

data = get_data()
spotify_data = data[0]
spotify_data['date'] = pd.to_datetime(spotify_data['date'])


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")


        st.title('Spotify - Analytics')

        if st.checkbox('Podcasts with more than 100 episodes'):
            episodes_more_than_X(spotify_data, 'show_name', 100)
            st.pyplot()
        st.text("")
        if st.checkbox('Trend over time'):
            plot_episodes_year(spotify_data, 'date')
            st.pyplot()
        st.text("")
        if st.checkbox('Distribution of length'):
            length_distribution(spotify_data, 'length(min)')
            st.pyplot()
        st.text("")
        if st.checkbox('Most similar words in w2v'):
            user_input = st.text_input("Topic (please enter up to two keywords)", 'Data Science')
            user_input = user_input.lower().replace(" ", "_")
            st.text("")
            plot_similar_words(model, user_input, 10)
            st.pyplot()

def episodes_more_than_X(data, column, number_of_episodes):
    '''Displays the number of episodes per podcaster'''
    episode_count = data[column].value_counts()
    episode_count = episode_count.where(lambda x : x>=number_of_episodes).dropna()
    episode_count = pd.DataFrame(episode_count)
    episode_count = episode_count.rename(columns={'show_name': 'Count'})

    plt.figure(figsize=(20,20))
    sns.barplot(episode_count.Count, episode_count.index)
    plt.xticks(np.arange(0, 500, 20), size=15)
    plt.yticks(size=15)
    plt.title(f'"Data Science" podcasts with more than {number_of_episodes} episodes',fontsize=25)
    plt.xlabel('Number of episodes', fontsize=15)
    sns.despine(bottom=True, left=True)
    return plt.show()

# length distribution
def length_distribution(data, column):
    plt.figure(figsize=(16,6))

    sns.kdeplot(data[column], shade = True, color = 'limegreen', legend = True )

    plt.title('Length of All "Data Science" Episodes', fontsize = 20)
    plt.xlabel('Length in Minutes', fontsize=16)
    plt.xticks(np.arange(0, 320, 10), size=10)
    plt.ylabel('Density', fontsize=16)
    plt.grid(color='#4d4d4d')
    return plt.show()

def plot_episodes_year(data, column):
    '''plot the episodes since the beginning'''
    x = data[column].dt.year
    sns.countplot(x=x, data=data)
    sns.despine(top=True, right=True, left=False, bottom=False)
    return plt.show

def plot_similar_words(model, user_input, topn):
    vocab = list(model.wv.vocab)
    X = model[vocab]

    top_10 = model.wv.similar_by_word(user_input, topn=topn)

    top_10 = [i[0] for i in top_10]
    Y = model[top_10]

    pca = PCA(n_components=3, random_state=42, whiten=True)
    clf = pca.fit_transform(Y)

    tmp = pd.DataFrame(clf, index=top_10, columns=['x', 'y', 'z'])
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(tmp['x'], tmp['y'], tmp['z'], alpha = 1)

    for word, row in tmp.iterrows():
        x, y, z = row
        pos = (x, y, z)
        ax.text(x, y, z, s=word, size=15, zorder=1, color='k')

    plt.title('w2v map - PCA')
    return plt.show()
