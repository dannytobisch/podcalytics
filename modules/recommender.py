'''Use of the recommendation system'''

from modules.get_data import get_data_spotify
#from modules.preprocessing import preprocessing, preprocessed_data
from modules.trainer import vectorization, kmeans, cluster_function, model
import pandas as pd
import gensim
from gensim.models import phrases, word2vec
from gensim.models import Word2Vec
#import nltk

model_w2v = Word2Vec.load("model/model_w2v.model")

def recommendation_system(user_input, n_cluster, data_preprocessed):
    # category = 'data science'
    # lang_input = 'en'

    # column_to_preprocess = 'title_and_description'

    number_of_clusters = n_cluster

    # # get the data from spotify
    # data = get_data_spotify(user_input=category, lang_input=lang_input)

    # # preprocess the data
    # data_preprocessed = preprocessed_data(data, column=column_to_preprocess)

    # change type of preprocessed column to use for tf-idf, keep other column to use for word2vec
    data_preprocessed['complete_processed_str'] = data_preprocessed['complete_processed'].astype('str') # generalize how the column is called
    data_vectorized = vectorization(data_preprocessed, 'complete_processed_str')

    # create labels
    labels = kmeans(data_vectorized, number_of_clusters)

    # assign clusters to relevant episode
    df_complete = cluster_function(labels, data_preprocessed)

    # merge clusters and data_vectorized for filtering in the next step
    vec_cluster = data_vectorized.merge(df_complete['cluster'], left_index=True, right_index=True)

    # create a dictionary that assigns topic to cluster
    matching = {}

    for i in range(0, number_of_clusters):
        cluster = vec_cluster[vec_cluster['cluster'] == i]
        c = model(cluster.drop(columns='cluster'))
        matching[i] = c[0]

    # match topics to respective cluster
    df_complete['topics'] = df_complete['cluster'].map(matching)

    # list all the topics
    topics = list(matching.values())

    '''new_topics_list =[]

    for topic in topics:
        temp_list = []
        new_topics_list.append(temp_list)
        for word in topic:
            temp_list.append(word.replace(" ", "_"))

    new_topics_list = pd.Series(new_topics_list)
    #Corp_pre = data_preprocessed.complete_processed.append(new_topics_list)
    # create corpus for word2vec
    #corpus = Corp_pre.values
    # automatically find word connections (bigrams in corpus)
    #bigrams = phrases.Phrases(corpus)
    model_w2v = Word2Vec.load("model/model_w2v.model")
    #model_w2v = word2vec.Word2Vec(bigrams[corpus], size=100, min_count=1, iter=20)'''

    #model_w2v = Word2Vec.load("model/model_w2v.model")
    dict_topics = {}
    for i in range (len(topics)):
        dict_topics[i] = topics[i]

    recommended_clusters = recommended_topic(user_input, list_of_topics=topics, dict_topics=dict_topics, model=model_w2v)[1]

    recommendations = recommended_episodes(recommended_clusters, df=df_complete)

    return recommendations
    #return new_topics_list

# function to return key for any value
def get_key(val, dict_topics):
    for key, value in dict_topics.items():
         if val == value:
                return key

    return 'key does not exist'

def recommended_topic(user_input, list_of_topics, dict_topics, model):

    distances = {}
    for word in list_of_topics:
        new_word = []
        for value in word:
            if value in list(model_w2v.wv.vocab):
                new_word.append(value)
            else:
              new_word.append('data')
        distances[get_key(word, dict_topics)] = model_w2v.wv.n_similarity(new_word, user_input.lower().split())
    top_3 = sorted(distances, key=distances.get, reverse=True)[:3]
    max_key = max(distances, key=distances.get)
    return max_key, top_3

def recommended_episodes(recommended_clusters, df):
    information = []
    for cl in recommended_clusters:
        temp = df[df['cluster'] == cl].sample(2)
        information.append(temp)
    final_df = pd.concat(information)
    return final_df

def recommendation_system_labeled(user_input, data_labeled):

    # list all the topics
    topics = list(data_labeled['topics'].unique())

    dict_topics = {}
    for i in range (len(topics)):
        dict_topics[i] = topics[i]

    recommended_clusters = recommended_topic(user_input, list_of_topics=topics, dict_topics=dict_topics, model=model_w2v)[1]

    recommendations = recommended_episodes(recommended_clusters, df=data_labeled)

    return recommendations
    #return new_topics_list

