import streamlit as st
import pandas as pd
import numpy as np
from pages.dashboard import get_data
import matplotlib.pyplot as plt
import seaborn as sns
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D
from wordcloud import WordCloud
from PIL import Image
import urllib
import requests


#audio_file = open('data/sound.mp3', 'rb')
#audio_bytes = audio_file.read()


# matplotlib.style.use('ggplot')
model = Word2Vec.load("model/model_w2v.model")

data = get_data()
arxiv_data = data[3]

cluster_list = list(arxiv_data['cluster'].value_counts().sample(n=3).index)

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    #with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")

    st.title('arXiv - Analytics')
    st.text("")
    if st.checkbox('Most similar words in w2v'):
        user_input = st.text_input("Topic (please enter up to two keywords)", 'Machine Learning')
        user_input = user_input.lower().replace(" ", "_")
        st.text("")
        number_of_similar_words = st.slider('Select a modulus', 3, 50)
        plot_similar_words(model, user_input, number_of_similar_words)
        st.pyplot()
    st.text("")
    if st.checkbox('Word Cloud'):
        cluster = st.slider('Select a cluster', 0, 49)
        word_cloud_kmeans(cluster)
        st.pyplot()

'''------------------------------------------------------------------'''
'''Functions to create the visualizations'''

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


def word_cloud_kmeans(cluster):
    slist =[]
    tmp_cluster = []
    text = arxiv_data[arxiv_data['cluster'] == cluster]['title']
    for x in text:
        slist.extend(x)
    text = [word for line in slist for word in line.split()]
    for word in text:
        string_list = ' '.join(word)
        tmp_cluster.append(string_list)
    cluster_new = ' '.join(tmp_cluster)
    wordcloud = WordCloud(background_color='white').generate(cluster_new)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
