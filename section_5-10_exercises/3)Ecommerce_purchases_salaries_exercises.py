#%%
import pandas as pd 
ecom = pd.read_csv('Ecommerce Purchases.csv')
ecom
# %%
#check the head of the data frame
ecom.head()
# %%
#how many rows and columns are there?
ecom.info()
# %%
ecom['Purchase Price'].mean()
# %%
#what was the highest and lowest purchase prices?
ecom['Purchase Price'].max()
# %%
ecom['Purchase Price'].min()

# %%
#how many people have english 'en' as their language of choice on the website?
ecom[ecom['Language'] =='en'].count()
# %%
#how many people have the job title of 'Lawyer'
ecom[ecom['Job'] == 'Lawyer'].info()
# %%
#how many people made the purchase during the AM and how many during the pm?
ecom['AM or PM'].value_counts()
#%%
#what are the 5 most common job titles?
ecom['Job'].value_counts().head(5)
# %%
#someone made a purchase that came from lot: '90 WT', what was the purchase price for this transaction?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']
# %%
#what is the email of the person with the following credit card number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
# %%
#how many people have American  Express as their credit card provider AND made a purchase above $95
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()
# %%
