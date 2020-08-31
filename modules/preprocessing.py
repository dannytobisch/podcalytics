'''Preprocess all the description to prepare for the model'''

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

# Define stop words and add update manually (if needed)
stop_words = stopwords.words('english')
newStopWords = ['podcast', 'episode', 'podcasts', 'also', 'itunes',\
                'like', 'u200d', 'twitter',\
                'dr', 'discus', 'vr']
stop_words.extend(newStopWords)

def preprocessing(X):
    '''Function to preprocess the episodes. Apply to a specific column such as
    episode descritption + episode name'''

    # lower case
    X = X.lower()

    # remove digits
    X = ''.join(word for word in X if not word.isdigit())

    # remove punctuation
    for punctuation in string.punctuation:
        X = X.replace(punctuation, '')

    # remove http and www
    X = re.sub(r'http\S+', '', X)
    X = re.sub(r'www\S+', '', X)
    # remove strings with two letters
    X = re.sub(r'\b\w{1,2}\b', '', X)

    # remove stop words
    word_tokens = word_tokenize(X)
    X = [w for w in word_tokens if not w in stop_words]

    # lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in X]
    X = lemmatized

    return X

def preprocessed_data(data, column):
    data['complete_processed'] = data[column].apply(preprocessing)
    # data['complete_processed'] = data['complete_processed'].astype('str')
    return data
