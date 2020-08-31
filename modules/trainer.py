'''Create a model'''
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans

tf_idf_vectorizer = TfidfVectorizer(ngram_range = (2,2), min_df = 0.01, max_df = 0.7)


def vectorization(df, column):
    '''Define the technique to vectorize the text for the model
    e.g. tf-idf, word2vec, etc.'''
    X = tf_idf_vectorizer.fit_transform(df[column])
    vectorized_data = pd.DataFrame(X.toarray(),columns = tf_idf_vectorizer.get_feature_names())
    return vectorized_data

def kmeans(df, n_clusters):
  '''Create clusters and output the labels'''
  km = KMeans(n_clusters=n_clusters, random_state=5)
  prediction_vector = km.fit_predict(df)
  return km.labels_


def cluster_function(labels, df):
  '''Create a new dataframe which contains episode_name, processed text and labels'''
  # cluster_map = pd.DataFrame()
  # cluster_map['data_index'] = original_df.episode_name.values
  # cluster_map['complete_processed'] = original_df.complete_processed.values
  # cluster_map['cluster'] = labels
  df['cluster'] = labels
  return df

def model(test):
    '''Run an LDA'''
    lda_model = LatentDirichletAllocation(n_components=1).fit(test)
    topics = []
    for idx, topic in enumerate(lda_model.components_):
#         print("Topic %d:" % (idx))
#         print([(tf_idf_vectorizer.get_feature_names()[i], topic[i])
#                         for i in topic.argsort()[:-10 - 1:-1]])
        topic_list = [tf_idf_vectorizer.get_feature_names()[i]
                        for i in topic.argsort()[:-3 - 1:-1]]
        topics.append(topic_list)
    return topics

# def space(test):
#     new_list = []
#     for text in test:
#         new_list.append(text.replace(" ", "_"))
#     return new_list


# def final_list(topics):
#     return [space(text) for text in topics]
