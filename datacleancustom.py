import pandas as pd

dfc = pd.read_csv("/Users/kerrafuller/Downloads/customers_500000.csv")
dfc['Index'] = dfc['Index'] - 1


print(dfc.head())