#%%
# import numpy as np
import numpy as np 

# %%
#create and array of 10 zeros
np.zeros(10)
# %%
np.ones(10)
# %%
np.ones(10) * 5
# %%
# create an array of the integers from 10 to 50
np.arange(10,51)
# %%
#create an array of the integers from 10 to 50 ( even numbers only)
np.arange(10,51,2)
# %%
#create a 3x3 matrix with values ranging from 0 to 8
np.arange(0,9).reshape(3,3)
# %%
#create a 3x3 identity matrix GOT THIS WRONG
np.eye(3)
# %%
#use numpy to generate a random number between 0 and 1 GOT THIS WRONG
np.random.rand(1)
# %%
#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution GOT THIS WRONG
np.random.rand(25)
# %%
#GOT THIS WRONG FORGOT TO RESHAPE IT TO TURN IT INTO A MATRIX RATHER THAN AN ARRAY
np.arange(0,101)/100
# %%
#create an array of 20 linearly spaced points between 0 and 1
#forgot to specify the last argument to have specifically 20 within the array
np.linspace(0,1,20)
# %%
mat = np.arange(1,26).reshape(5,5)
mat
# %%
mat[3:,2:]
# %%
mat[2:,1:]
# %%
