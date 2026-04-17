import pandas as pd

dfo = pd.read_csv('/Users/kerrafuller/Downloads/organizations_500000.csv')
dfo['Index'] = dfo['Index'] - 1
dfo = dfo.drop(columns=['Organization Id'])

#ORGANIZE INDUSTRY
dfo['Industry'] = dfo['Industry'].str.split().str[0]
dfo_industry = dfo.groupby('Industry').size()

#SORT YEARS AND EMPLOYES
dfo['Rounded Employees'] = dfo['Number of employees'].round(-3)
dfo['Rounded Founded'] = dfo['Founded'].round(-1)

dfo_employees = dfo.groupby('Rounded Employees').size()
dfo_founded = dfo.groupby('Rounded Founded').size()


#VERIFY WEBSITES
website_start_pattern = r'^(https?://|www\.)'
website_end_pattern = r'\.(com|org|net|edu|gov|io|co)(/|$)'
start_mask = dfo['Website'].str.match(website_start_pattern, na=False)
end_mask = dfo['Website'].str.contains(website_end_pattern, na=False)
dfo_valid_websites = dfo[start_mask & end_mask]



print(dfo.head(n=20))
