#%%
import numpy as np
import pandas as pd 
from numpy.random import randn
np.random.seed(101)
# %%
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df
# %%
#IN PANDAS WE CAN USE CONDITONAL SELECTION
booldf = df > 0 #this will return boolean values to the each cells 
booldf
# %%
df[booldf]#this will return the data sets that are true and return Nan for the ones that were false
df[df>0] #this will work as well

# %%
df
# %%
df['W' ] > 0
# %%
df[df['W'] > 0]#with our condition since row C is false it was not returned
# %%
df[df['Z'] < 0]
# %%
#since the two examples above returned a data frame, we can then use that returned data frame to create additional commands
resultdf = df[df['W'] > 0]
resultdf # resultdf is the table returned after passing our condition showing that we can use resultdf to further manipulate the table
# %%
resultdf['X']
# %%
df[df['W'] > 0]['X']#this is the same as resultdf['X]
# %%
df[df['W'] > 0][['Y','X']]
# %%
#below will be examples using multiple conditions
df[df['W'] > 0] and (df['Y'] > 1) # using the `and` operator this way will result in an error
# %%
df[df['W'] > 0 & (df['Y'] > 1)] #we need to the `&` symbol instead of `and `

# %%
df[df['W'] > 0 | (df['Y'] > 1)] #this is for an `or` condition.
# %%
#below are ways to reset the index or setting it to something else

df.reset_index() #this method will change the index back into numbers and the labels will now be in a new column labeld as "index" aka resetting the index
# %%
newind = ' CA NY WY OR CO'.split() #quicker way to create a list without having to type all of the commas 
newind
# %%
df['States'] = newind
df
# %%
df.set_index('States')#this will change the label of the index
# %%
