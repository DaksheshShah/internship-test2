# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:26:09 2021

@author: Dakshesh
"""

import pandas as pd

df=pd.read_csv('input/question-3/main.csv',usecols = ['Team','Yellow Cards','Red Cards'])


sorted_df = df.sort_values(by=["Red Cards","Yellow Cards"], ascending=[False,False])
sorted_df.to_csv('output/answer-3/answer3.csv')
print(sorted_df)