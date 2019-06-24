# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:10:32 2019

@author: hp
"""
"""
Q1. (Create a program that fulfills the following specification.)

Program Specification

Use the prev. ANN model to predict if the customer with the following information will leave the bank: (Churn_Modelling.csv)

        Geography: France
        Credit Score: 600
        Gender: Male
        Age: 40 years old
        Tenure: 3 years
        Balance: $60000
        Number of Products: 2
        Does this customer have a credit card? Yes
        Is this customer an Active Member: Yes?
        Estimated Salary: $50000

So, should we say goodbye to that customer?
"""
import pandas as pd
dataset=pd.read_csv("Churn_Modelling.csv")
features = dataset.iloc[:, 3:13].values
labels = dataset.iloc[:, 13].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_features_1 = LabelEncoder()
features[:, 1] = labelencoder_features_1.fit_transform(features[:, 1])

labelencoder_features_2 = LabelEncoder()
features[:, 2] = labelencoder_features_2.fit_transform(features[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:]