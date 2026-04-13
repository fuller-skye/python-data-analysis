import pandas as pd


df1 = pd.read_csv('/Users/kerrafuller/Downloads/people_500000.csv')
df1['Index'] = df1['Index'] - 1 


#TASKS
#ORDER NAMES IN ALPHABETICAL ORDER
dfp = dfp.sort_values(by='First Name', ascending=True)


#CLEAN UP PHONE NUMBERS TO BE IN THE FORMAT (XXX) XXX-XXXX
dfp['Phone'] = dfp['Phone'].str.replace(r'x.*$', '', regex=True)
dfp['Phone'] = dfp['Phone'].str.replace('001-', '', regex=False)
dfp['Phone'] = dfp['Phone'].str.replace(r'(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})', r'(\1)-\2-\3', regex=True)


#CREATE COLUMN FOR YEAR OF BIRTH
dfp['Year born'] = [str(val)[:4] for val in dfp['Date of birth']]


#COMBINE FIRST AND LAST NAME INTO A FULL NAME COLUMN
dfp['Full Name'] = dfp['First Name'] + ' ' + dfp['Last Name']
dfp = dfp.drop(columns=['First Name', 'Last Name'])

print(dfp.head(n=10))

#SORT BY JOB TITLE



#SORT BY SEX


#SORT BY YEAR OF BIRTH


#FIND AVG YEAR OF BIRTH

