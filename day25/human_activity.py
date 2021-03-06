# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:48:25 2019

@author: hp
"""
"""
Q1. Human Activity Recognition

Human Activity Recognition with Smartphones

(Recordings of 30 study participants performing activities of daily living)

(Click Here To Download Dataset): "https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip"



In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, each person performed six activities (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. The experiments have been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data.

 

Attribute information 

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set. Compare the results. Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature selection.
        
"""
import pandas as pd
import numpy as np
df=pd.read_csv("test.csv")
df1=pd.read_csv("train.csv")
features_train=df.iloc[:,:-1].values
labels_train=df.iloc[:,-1].values
features_test=df1.iloc[:,:-1].values
labels_test=df1.iloc[:,-1].values
#decision tree
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test) 
from sklearn.metrics import confusion_matrix,accuracy_score 
print(confusion_matrix(labels_test, labels_pred))  
print(accuracy_score(labels_test, labels_pred))
score1=classifier.score(features_test,labels_test)
score2=classifier.score(features_train,labels_train)
#random forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred2 = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix,accuracy_score 
print(confusion_matrix(labels_test, labels_pred2))  
score3=classifier.score(features_test,labels_test)
score4=classifier.score(features_train,labels_train)
#Logistic regression......................
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
score5=classifier.score(features_test,labels_test)
#knn approach.................
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
score6=classifier.score(features_test,labels_test)
#features_selection.............................
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
labels_train=le.fit_transform(labels_train)
import statsmodels.api as sm

list1=[]
list2=[]
for i in range(0,563):
    list1.append(i)
    list2.append(i)
features_train = np.append(np.ones((2947,1)), features_train, axis=1)   
features_opt=features_train[:,list1]    
regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
list1=[]
list1=list(regressor_OLS.pvalues)
while max(list1) > 0.05:
    index=list1.index(max(list1))
    list2.remove(list2[index])
    features_opt=features_train[:,list2]
    regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
    list1=list(regressor_OLS.pvalues)
    
