#%%
#import pandas as pd
from numpy.core.fromnumeric import sort
import pandas as pd 

# %%
sal = pd.read_csv('Salaries.csv')
sal
# %%
#run the head of sal
sal.head()
# %%
#get info from sal
sal.info()
# %%
#what is the average basepay
sal['BasePay'].mean()
# %%
#What is the highest amount of overtimepay in the data set?
sal
# %%
sal['OvertimePay'].max()
# %%
#whatis the job title of JOSEPH DRISCOLL?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
# %%
#how much does JOSEPH DRISCOLLE make (including benefits)
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
# %%
#What is the name of the highest paid person (including benefits)?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
# %%
#what is the name of the lowest paid person(including benefits)? Do you notice something s trange about how much he or she is paid?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
# %%
#what was the average (mean) basepay of all employees per year? (2011 - 2014)
sal.groupby('Year').mean()['BasePay']
# %%
#how many unique job titles are there?
sal['JobTitle'].nunique()
# %%
#what are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# %%
#How many job titles were represented by one person in 2013?
sal
# %%
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

# %%
