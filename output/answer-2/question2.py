# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:19:58 2021

@author: Dakshesh
"""

import pandas as pd

df=pd.read_csv('input/question-2/main.csv')


#FINDING MAX AND MIN
p=df['age'].max()
q=df['age'].min()

df = df.groupby('occupation').agg({'age':['min','max']})
df.to_csv('output/answer-2/answer2.csv',index=False)
print(df)