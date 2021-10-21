# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:19:58 2021

@author: Dakshesh
"""

import pandas as pd
import numpy as np
df = pd.read_csv('input/question-1/main.csv')


years_sum =  df.groupby(np.floor((df['Year']/10))).agg({'Violent':'sum','Property':'sum','Murder':'sum','Forcible_Rape':'sum','Robbery':'sum','Aggravated_assault':'sum','Burglary':'sum','Larceny_Theft':'sum','Vehicle_Theft':'sum'})
years_sum.to_csv('output/answer-1/answer1.csv',index=False)
print(years_sum)