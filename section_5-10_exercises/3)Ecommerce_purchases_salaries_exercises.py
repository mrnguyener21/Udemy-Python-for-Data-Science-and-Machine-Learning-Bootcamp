#%%
import pandas as pd 
ecom = pd.read_csv('Ecommerce Purchases.csv')
ecom
# %%
#check the head of the dataframe
ecom.head()
# %%
#how many rows and columns are there
ecom.info()
# %%
#what is the average purchase price
ecom['Purchase Price'].mean()
# %%
#what was the highest price
ecom['Purchase Price'].max()
# %%
#what was the lowest price
ecom['Purchase Price'].min()
# %%
#how many people have 'en' as their language of choice on the website?
ecom[ecom['Language'] == 'en'].count()
# %%
ecom[ecom['Job'] == 'Lawyer'].info()
# %%
#how many people made the purhase during the AM and how many people made the purcahse during the PM
ecom['AM or PM'].value_counts()
# %%
#what are the 5 most common job titles
ecom['Job'].value_counts().head(5)
# %%
#someone made a purchase that came from lot: '90 WT', what was the purchase price for this transaction?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']
# %%
#what is the email of the person  with the following credit card number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
# %%
#how many people have America Express as ttheir Credit Card Provider and made a purcahse above $95?
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()
# %%
