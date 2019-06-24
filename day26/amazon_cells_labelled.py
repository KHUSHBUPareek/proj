# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:13:50 2019

@author: hp
"""
"""
Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt


The Data has sentences from Amazon Reviews

Each line in Data Set is tagged positive or negative

Create a Machine learning model using Natural Language Processing that can predict wheter a given review about the product is positive or negative
"""
import numpy as np
import pandas as pd
df=pd.read_csv("amazon_cells_labelled.txt",delimiter='\t',header=None)
df.columns=['Review','Liked']

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 


corpus = []

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
    
#check
review="Good case, Excellent value."
review = re.sub('[^a-zA-Z]', ' ', review)
review = review.lower()
review = review.split()

review = [word for word in review 
          if not word 
          in set(stopwords.words('english'))]
    
#lem = WordNetLemmatizer() #Another way of finding root word
ps = PorterStemmer()
review = [ps.stem(word) for word in review]
#review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
review = ' '.join(review)

review=cv.transform([review]).toarray()
classifier.predict(review)
