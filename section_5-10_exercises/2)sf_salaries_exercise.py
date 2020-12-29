#%%
import pandas as pd 
sal = pd.read_csv('Salaries.csv')
sal
# %%
sal.head()
# %%
sal.info()
# %%
#What is the average base pay
sal['BasePay'].mean()
# %%
#what ist he highest amoutof overtime pay in the dataset?
sal
# %%
sal['OvertimePay'].max()
# %%
#what is the job title of JOSEPH DRISCOLL?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
# %%
#how much does joseph dricoll make(including benefits)
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
# %%
#What is the name of the highestt paid person9including benefits
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
# %%
#what is the name of the lowest paid person(incluing benefits)?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
# %%
sal['Year']
# %%
sal.groupby('Year').mean()['BasePay']
# %%
#how many unique job titles are there?
sal['JobTitle'].nunique()
# %%
sal['JobTitle'].value_counts().head(5)
# %%
#how many job titles were represented by only one person in 2013?
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

# %%
#how many people have the word chief in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
        
sum(sal['JobTitle'].apply(lambda x: chief_string(x)))
# %%
