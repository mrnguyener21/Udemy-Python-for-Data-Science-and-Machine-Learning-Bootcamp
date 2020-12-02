#%%
#data frames is the main tool in pandas
import numpy as np
import pandas as pd 
from numpy.random import randn
np.random.seed(101)
# %%
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df
#These are just a bunch of series(the columns/second argument) that share a common index(first array/argument)
# %%
df['W']#Doing this will grab the W series
# %%
df[['W','X']] #THIS IS HOW YOU CALL MULTIPLE COLUMNS
# %%
#BELOW IS AN EXAMPLE OF HOW TO ADD A NEW COLUMN
df['new'] = df['W']  + df['Y']
df
# %%
#BELOW IS AN EX OF HOW TO DROP A COLUMN
df.drop('new', axis = 1, inplace = True)
#df.drop does not affect the data frame unless we specify it to occur inplace (third arguement)
#this is done as a fail safe from accidentally losing data
df
# %%
df.drop('E') #we can do it with indexes as well
# %%
df.shape
# %%
#BELOW IS HOW WE SELECT ROWS BASED ON THE LABEL OF THE INDEX
df.loc['A']# the rows are series as well when returned from a request with pandas
# %%
#BELOW IS HOW WE SELECT ROWS BASED ON THE INDEX POSITION
df.iloc[0]
# %%
#THIS IS HOW TO SELECT SUBSET OF ROWS AND COLUMNS
df.loc['B','Y']# in this ex we get what is positioned at row B column Y
df.loc[['A','B'],['W','Y']]#in this ex we get what is positioned within two rows and two columns
# %%
