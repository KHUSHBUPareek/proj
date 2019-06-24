# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:52:13 2019

@author: hp
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:29:15 2019

@author: hp
"""
"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
"""
import numpy as np
import pandas as pd
#data.json
with open("data.json") as f:
    data = f.read()
data = data[data.find("[{"):]
df = pd.read_json(data)
#test1.json
file = open("test1.json", encoding="utf8")
data1=file.read()
data1 = data1[data1.find("{"):]
df1 = pd.read_json(data1,lines=True)
features=df.iloc[:,[1,3]].values
labels=df.iloc[:,1].values
features_test=df1.iloc[:,[0,2]].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features[:,0]=le.fit_transform(features[:,0])
le1=LabelEncoder()
features[:,1]=le1.fit_transform(features[:,1])
le3=LabelEncoder()
features_test[:,0]=le3.fit_transform(features_test[:,0])
le4=LabelEncoder()
features_test[:,1]=le4.fit_transform(features_test[:,1])

#nlp
import re
import nltk
nltk.download('stopwords')
corpus=[]
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer    
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', df['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]   
    ps =PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features2 = cv.fit_transform(corpus).toarray()
featur=np.append(features,features2,axis=1)
#for test heading
corpus1=[]
for i in range(0,15370):
    review1 = re.sub('[^a-zA-Z]', ' ', df1['heading'][i])
    review1 = review1.lower()
    review1 = review1.split()
    review1 = [word for word in review1 if not word in set(stopwords.words('english'))]   
    ps =PorterStemmer()
    review1 = [ps.stem(word) for word in review1]
    review1 = ' '.join(review1)
    corpus1.append(review1)

#from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features3 = cv.fit_transform(corpus1).toarray()
featur2=np.append(features_test,features3,axis=1)
le6=LabelEncoder()
labels=le6.fit_transform(labels)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(featur,labels)
lb=dt.predict(featur2)    
