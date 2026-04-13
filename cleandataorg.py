import pandas as pd

dfo = pd.read_csv('/Users/kerrafuller/Downloads/organizations_500000.csv')
dfo['Index'] = dfo['Index'] - 1

print(dfo.head())
