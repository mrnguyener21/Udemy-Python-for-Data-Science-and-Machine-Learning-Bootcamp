#%%
import pandas as pd 
ecom = pd. read_csv('Ecommerce Purchases.csv')
ecom
# %%
#check the head oft he data frame
ecom.head()
# %%
#how many rows and columns are there
ecom.info()
# %%
#What is the average purchase price
ecom['Purchase Price'].mean()
#%%
# What is the highest purchase price
ecom['Purchase Price'].max()

# %%
#what is the lowest purchase price
ecom['Purchase Price'].min()

# %%
#how many people have English 'en' as their language of choice on the website
ecom[ecom['Language'] == 'en'].count()
# %%
#how many people have the job title of 'Lawyer'?
ecom[ecom['Job'] == 'Lawyer'].info()
# %%
#how many people made the purchase during the AM and how many during the PM
ecom['AM or PM'].value_counts()
# %%
 #what are the most common job titles
ecom['Job'].value_counts().head(5)
# %%
#someone made a purchase that came from lot: "90 WT", what waas the purchase price for this transaction?
ecom
# %%
ecom[ecom['Lot'] == '90 WT']['Purchase Price']
# %%
#what is the email of the person with the following credit card number:4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
# %%
#how many people have American Express as their credit card provider and made a purcahse above $95?
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()
# %%
#how many people have a credit card that expires in 2025
ecom
# %%
sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')
# %%
