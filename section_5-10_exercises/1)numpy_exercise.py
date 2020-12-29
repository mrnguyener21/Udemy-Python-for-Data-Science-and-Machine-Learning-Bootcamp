#%%
#import numpy as np
import numpy as np

# %%
#create an a4rray of 10 zeros
np.zeros(10)
# %%
#create an array of 10 ones
np.ones(10)
# %%
#create an array of 10 fives
np.ones(10)*5
# %%
#createan array of the integers from 10 to 50
np.arange(10,51)
# %%
#create an array of all the even integers from 10 to 50
np.arange(10,51,2)
# %%
np.arange(0,9).reshape(3,3)
# %%
#use numpy to generate a random number between 0 and 1
np.random.rand(1)
# %%
np.arange(1,101).reshape(10,10)/100
# %%
mat = np.arange(1,26).reshape(5,5)
mat
# %%
mat[2:,1:]
# %%
mat[3,4]
# %%
mat[:3,1:2]
# %%
mat
# %%
mat[4:,0:]
# %%
mat[3:,0:]
# %%
#get the sum of all the values in mat
mat.sum()
# %%
mat.std()
# %%
mat.sum(axis=0)
# %%
