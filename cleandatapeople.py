import pandas as pd


df1 = pd.read_csv('/Users/kerrafuller/Downloads/people_500000.csv')
df1['Index'] = df1['Index'] - 1 

print(df1.head())
