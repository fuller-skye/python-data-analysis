import pandas as pd

dfp = pd.read_csv('/Users/kerrafuller/Downloads/people_500000.csv')
dfa = pd.read_csv('/Users/kerrafuller/Downloads/us-area-code-cities.csv')
dfp['Index'] = dfp['Index'] - 1 
dfp = dfp.drop(columns=['User Id'])
dfp = dfp.drop(columns=['Email'])

#TASKS
#ORDER NAMES IN ALPHABETICAL ORDER
dfp = dfp.sort_values(by='First Name', ascending=True)

#CLEAN UP PHONE NUMBERS TO BE IN THE FORMAT (XXX) XXX-XXXX
dfp['Phone'] = dfp['Phone'].str.replace(r'x.*$', '', regex=True)
dfp['Phone'] = dfp['Phone'].str.replace('001-', '', regex=False)
dfp['Phone'] = dfp['Phone'].str.replace(r'(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})', r'(\1)\2-\3', regex=True)
dfp['Phone'] = dfp['Phone'].str.replace('+1-', '', regex=False)

#ISOLATE AREA CODE
dfp['Area Code'] = dfp['Phone'].str.extract(r'\((\d{3})\)')
dfp['Area Code'] = dfp['Area Code'].astype(str)

#VALIDATE AREA CODE
dfa_valid_area_code = dfa.groupby('201').size()
dfp = dfp[dfp['Area Code'].isin(dfa_valid_area_code.index.astype(str))]
dfp = dfp.sort_values(by='Area Code', ascending=True)

#CREATE COLUMN FOR YEAR OF BIRTH
dfp['Year born'] = [str(val)[:4] for val in dfp['Date of birth']]
dfp['Year born'] = [int(val) for val in dfp['Year born']]
#FIND AVG AGE AND FILTER OUT PEOPLE OLDER THAN THE AVG AGE
dfp_age_avg = (dfp['Year born'].mean())
dfp = dfp[dfp['Year born'] >= dfp_age_avg]

#COMBINE FIRST AND LAST NAME INTO A FULL NAME COLUMN
dfp['Full Name'] = dfp['First Name'] + ' ' + dfp['Last Name']
dfp = dfp.drop(columns=['First Name', 'Last Name'])

#GROUP BY JOB TITLE
dfp['Job Title'] = dfp['Job Title'].str.split().str[0]
dfp['Job Title'] = dfp['Job Title'].str.replace(',', '', regex=False)
dfp_job_title = dfp.groupby('Job Title').size()

#GROUP BY SEX
dfp_sex = dfp.groupby('Sex').size()

#GROUP BY YEAR OF BIRTH
dfp_year_born = dfp.groupby('Year born').size()

#GROUP BY AREA CODE
dfp_area_code = dfp.groupby('Area Code').size()

#RESORT BY INDEX
dfp = dfp.sort_values(by = 'Index', ascending = True)


print(dfp)


