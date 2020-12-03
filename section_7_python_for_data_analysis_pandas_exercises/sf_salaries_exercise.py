#%%
#import pandas as pd 
import pandas as pd
from pandas.core.arrays.base import ExtensionScalarOpsMixin 

# %%
#Read Salaries.csv as a dataframe called sal.
salaries = pd.read_csv(r'C:\Users\vnguyen\OneDrive - Tricon Residential\Documents\Refactored_Py_DS_ML_Bootcamp-master\04-Pandas-Exercises\Salaries.csv')
salaries
# %%
#check the head of the DataFrame
salaries.head()
# %%
#use the info method to find out how many entries there are
salaries.info()
# %%
#what is the average BasePay?
salaries['BasePay'].mean()
# %%
#what is the highest amount of overtimepay in the dataset
salaries['OvertimePay'].max()
# %%
#what is the job title of JOSEPH DRISCOLL?
salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# %%
# How much does JOSEPH DRISCOLL MAKE INCLUDING BENEFITS
salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# %%
#What is the name of highest paid person (including benefits)?
# salaries[salaries['TotalPayBenefits'].max()]['EmployeeName']
salaries[salaries['TotalPayBenefits']== salaries['TotalPayBenefits'].max()]
# %%
salaries['TotalPayBenefits'].max()# %%

# %%
#What is the name of the lowest paid person including benefits
salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()]
# %%
#what was the average(mean) basepay of all employees per year? (2011- 2014)
#we want the mean for each year
salaries.groupby('Year').mean()['BasePay']
# %%
salaries['JobTitle'].nunique()
# %%
#what are the top 5 most common jobs
#group by job
#sort from highest to lowest
#only return the top 5
salaries['JobTitle'].value_counts().head(5)
# %%
#how many job titles were represented by only one person in 2013?
sum(salaries[salaries['Year'] == 2013]['JobTitle'].value_counts() == 1)
# %%
#how many people have the word chief in their job title?
salaries['JobTitle'].__contains__('Chief')
# %%
