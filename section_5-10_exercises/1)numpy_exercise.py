#%%
#import numpy as np
import numpy as np 

# %%
np.zeros(10)
# %%
#createa an array of 10 ones
np.ones(10)
# %%
#create an array of 10 fives
np.ones(10) * 5
# %%
#create an array of the integers froom 10 to 50
np.arange(0,51)
# %%
#create an array of all the even integers from 10 to 60
np.arange(0,51,2)
# %%
#create a 3x3 matrix with values ranging from 0 t0 8
np.arange(0,9).reshape(3,3)
# %%
#create a 3x3 identity matrix
np.identity(3)
# %%
#use numpy to generate a random number between 0 and 1
np.random.rand(1)
# %%
#use numpy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.rand(25)
# %%
np.arange(1,101).reshape(10,10)/100
# %%
#create an array of 20 linearly spaced points betwen 0 and 1
np.linspace(0,1)
# %%
mat = np.arange(1,26).reshape(5,5)
mat
# %%
mat[2:,1:]
# %%
mat[:3,1:2]
# %%
mat[3:]
# %%
mat.sum()
# %%
mat.std()
# %%
mat.sum(axis=0)
# %%
