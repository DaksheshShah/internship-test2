
import pandas as pd
df = pd.read_csv('input/question-1/main.csv')
filter = df["Year"]%10 == 0
df.where(filter, inplace = True)
df = df.dropna()
df.to_csv('output/answer-1/answer1.csv',index=False)
print(df)