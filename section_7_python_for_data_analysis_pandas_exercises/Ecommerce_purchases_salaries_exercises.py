#%%
import numpy as np
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
#what is the average purchase price?
ecom['Purchase Price'].mean()

# %%
#what were the highest and lowest purchase prices?
ecom['Purchase Price'].max()
# %%
ecom['Purchase Price'].min()
# %%
ecom[ecom['Language'] == 'en'].count()
# %%
# %%
ecom[ecom['Job'] == 'Lawyer'].info()
# %%
#how many people made the purchase during the AM and how many people made the purchase during the PM
ecom['AM or PM'].value_counts()
# %%
#what are the 5 most common Job Titles?
ecom['Job'].value_counts().head(5)
# %%
#Someone made a purchase that came from Lot: '90WT',what was the purchase price for this transaction?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']
# %%
#what is the email of the person with the following credit card number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
# %%
#How many people have American Express as their Credit Card Provider and made a purchase above $95?
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95) ].count()
# %%
#how many people have a credit card that expires in 2025
#NEED TO LOOK AT SOLUTION VIDEO FOR EXPLANATION
# %%
ecom['Email']
# %%
#NEED TO LOOK AT SOLUTIONS VIDEO FOR EXPLANATION