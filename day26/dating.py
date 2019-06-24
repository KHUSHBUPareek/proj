# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:57:43 2019

@author: hp
"""
"""
Q2. Code Challenge (Connecting Hearts)


Downlaod Link: http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/Resource.zip

What influences love at first sight? (Or, at least, love in the first four minutes?) This dataset was compiled by Columbia Business School Professors Ray Fisman and Sheena Iyengar for their paper Gender Differences in Mate Selection: Evidence from a Speed Dating Experiment.

Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.


What does a person look for in a partner? (both male and female)


For example: being funny is more important for women than man in selecting a partner! Being sincere on the other hand is more important to men than women.

    What does a person think that their partner would look for in them? Do you think what a man thinks a woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

    Plot Graphs for:
            How often do they go out (not necessarily on dates)?
            In which activities are they interested?
    
    If the partner is from the same race are they more keen to go for a date?
    What are the least desirable attributes in a male partner? Does this differ for female partners?
    How important do people think attractiveness is in potential mate selection vs. its real impact?
"""    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
df1=pd.read_csv("Dating_Data.csv",encoding = 'unicode_escape') 
att_m=df1.groupby('gender')['pf_o_att'].sum()[1]
att_f=df1.groupby('gender')['pf_o_att'].sum()[0]
sin_m=df1.groupby('gender')['pf_o_sin'].sum()[1]
sin_f=df1.groupby('gender')['pf_o_sin'].sum()[0]
int_m=df1.groupby('gender')['pf_o_int'].sum()[1]
int_f=df1.groupby('gender')['pf_o_int'].sum()[0]
fun_m=df1.groupby('gender')['pf_o_fun'].sum()[1]
fun_f=df1.groupby('gender')['pf_o_fun'].sum()[0]
amb_m=df1.groupby('gender')['pf_o_amb'].sum()[1]
amb_f=df1.groupby('gender')['pf_o_amb'].sum()[0]
sha_m=df1.groupby('gender')['pf_o_sha'].sum()[1]
sha_f=df1.groupby('gender')['pf_o_sha'].sum()[0]
list1=[att_m,sin_m,int_m,fun_m,amb_m,sha_m]
max(list1)#int_m
min(list1)#sha_m
list2=[att_f,sin_f,int_f,fun_f,amb_f,sha_f]
max(list2)
min(list2)#amb_f
#What does a person think that their partner would look for in them? Do you think what a man thinks a woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)
att2_m=df1.groupby('gender')['attr2_1'].sum()[1]
att2_f=df1.groupby('gender')['attr2_1'].sum()[0]
sin2_m=df1.groupby('gender')['sinc2_1'].sum()[1]
sin2_f=df1.groupby('gender')['sinc2_1'].sum()[0]
int2_m=df1.groupby('gender')['intel2_1'].sum()[1]
int2_f=df1.groupby('gender')['intel2_1'].sum()[0]
fun2_m=df1.groupby('gender')['fun2_1'].sum()[1]
fun2_f=df1.groupby('gender')['fun2_1'].sum()[0]
amb2_m=df1.groupby('gender')['amb2_1'].sum()[1]
amb2_f=df1.groupby('gender')['amb2_1'].sum()[0]
sha2_m=df1.groupby('gender')['shar2_1'].sum()[1]
sha2_f=df1.groupby('gender')['shar2_1'].sum()[0]
list3=[att2_m,sin2_m,int2_m,fun2_m,amb2_m,sha2_m]
max(list3)#att2_m
list4=[att2_f,sin2_f,int2_f,fun2_f,amb2_f,sha2_f]
max(list4)#att2_f
a=df1['go_out'].value_counts()
label=(a).index
values=(a).values
plt.bar(label,values)
plt.xlabel("no. of times")
plt.ylabel("dates")
s=df1['sports'].sum()
e=df1['exercise'].sum()
t=df1['tvsports'].sum()
d=df1['dining'].sum()
m=df1['museums'].sum()
a=df1['art'].sum()
h=df1['hiking'].sum()
g=df1['gaming'].sum()
c=df1['clubbing'].sum()
r=df1['reading'].sum()
t=df1['tv'].sum()
th=df1['theater'].sum()
mo=df1['movies'].sum()
c=df1['concerts'].sum()
mu=df1['music'].sum()
sh=df1['shopping'].sum()
y=df1['yoga'].sum()
list5=[s,e,t,d,m,a,h,g,c,r,t,th,mo,c,mu,sh,y]
max(list5)
labels2=['s','e','t','d','m','a','h','g','c','r','t','th','mo','c','mu','sh','y']
plt.bar(labels2,list5)
plt.xlabel("ACTIVITY INTERESTED")
a=df1['imprace'].value_counts()
