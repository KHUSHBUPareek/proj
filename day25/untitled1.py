# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:17:23 2019

@author: hp
"""

"""        
Q2. Code Challenge

#Online Marketing

(Click Here To Download Resource File) : http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/online_marketing.sql

Objective of this case study is to explore Online Lead Conversion for a Life Insurance company. Some people are interested in buying insurance products from this company hence they visit the site of this Life Insurance Company and fill out a survey asking about attributes like income, age etc. These people are then followed and some of them become customers from leads. Company have all the past data of who became customers from lead. Idea is to learn something from this data and when

some new lead comes, assign a propensity of him/her converting to a customer based on attributes asked in the survey. This sort of problem is called as Predictive Modelling

Concept:

Predictive modelling is being used by companies and individuals all over the world to extract value from historical data. These are the mathematical algorithms, which are used to "learn" the patterns hidden on all this data. The term supervised learning or classification is also used which means you have past cases tagged or classified (Converted to Customer or Not) and you want to use this learning on new data. (machine learning)

Here are the attributes of the survey:

Attribute

age (Age of the Lead)

Job (Job Category e.g. Management)

marital (Marital Status)

education (Education of Lead)

smoker (Is Lead smoker or not (Binary – Yes / No))

monthlyincome (Monthly Income)

houseowner (Is home owner or not (Binary – Yes / No))

loan (Is having loan or not (Binary – Yes / No))

contact (Contact type e.g. Cellphone)

mod (Days elapsed since survey was filled)

monthlyhouseholdincome (Monthly Income of all family member)

target_buy (altogether Is converted to customer or not (Binary –Yes /No). This is known as Target or Responseand this is what we are modelling.)



Activities you need to perform:


a. Handle the missing data and perform necessary data pre-processing.
b. Summarise the data.
c. Perform feature selection and train using prediction model.
d. For a new lead, predict if it will convert to a successful lead or not.
e. Use different classification techniques and compare accuracy score and also plot them in a bar graph.
"""
import os
import mysql.connector
import pandas as pd
import numpy as np
from pandas import DataFrame
# connect to  MySQL server along with Database name
conn=mysql.connector.connect(user='khushbu', password='9460535599Krish@',
                              host='db4free.net', database = 'khushbu1')
query="select * from online_marketing"

df=pd.read_sql(query,conn)
#df.isnull().any()
df1=pd.get_dummies(df) 
features=df1.iloc[:,:-1].values
labels=df1.iloc[:,-1].values
import statsmodels.formula.api as sm
features_obj = np.append(np.ones((3786,1)), features, axis=1)
features_opt = features_obj[:, [0,1,2,3,4,5,6,7,8,9,10]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
 
list1=[0, 1, 2,3,4,5,6,7,8,9,10]
list2=list(regressor_OLS.pvalues)
while max(list2) > 0.005:
    index=list2.index(max(list2))
    list1.remove(list1[index])
    list2.remove(list2[index])
    features_opt=features[:,list1]























































































































