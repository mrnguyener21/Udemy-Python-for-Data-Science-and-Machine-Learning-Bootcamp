#%%
from numpy import testing
import pandas as pd 
pd
# %%
sal = pd.read_csv('Salaries.csv')
sal
# %%
#cheeck the head of the data fram
sal.head()
# %%
sal.info()
# %%
sal['BasePay'].mean()
# %%
#wat is the highest amount of overtiem pay in the dataset?
sal['OvertimePay'].max()
# %%
#what is the job title of JOSEPH DRISCOL?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
# %%
#what is the name of the highest paid person(including benefits
# sal[sal['TotalPayBenefits'].max()].head(1)
#Below is the correct answer
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
# %%
#what is the nae of the lowest paid person(includingg benefits?) Do you notice something strange about how much he or she is paid?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
# %%
#what was the average(mean) basepay of all employees per year?
sal
# %%
sal.groupby('Year')['BasePay'].mean()
# %%
#how many unique job titls are there?
sal['JobTitle'].nunique()
# %%
sal['JobTitle'].value_counts().head(5)
# %%
#how many job titles were represented by only one person in 2013?
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
