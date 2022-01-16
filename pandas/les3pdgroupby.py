import pandas as pd 

data = {'Job': ['Data Mining','CEO','Lawyer','Lawyer','Data Mining','CEO'],'Labouring': ['Immanuel','Jeff','Olivia','Maria','Walker','Obi-Wan'], 'Salary': [4500,30000,6000,5250,5000,35000]}

df = pd.DataFrame(data)
SalaryGroupBy = df.groupby('Salary')
result = df.groupby('Job').sum().loc['CEO']
result = df.groupby('Job').count()
result = df.groupby('Job').mean()['Salary']['CEO']
print(result)