#%%
#exercise 1: import numpy as np
import numpy as np
# %%
#exercise 2 create an arry of 10 zeros
np.zeros(10)
# %%
#exercise 3 create an array of 10 ones
np.ones(10)
# %%
#create an array of 10 fives
np.ones(10) * 5

# %%
# create an array of the integers from 10 to 50
np.arange(10,51)
# %%
#create an array of all the even integers from 10 to 50
np.arange(10,51,2)
# %%
# create a 3x3 matrix with values ranging from 0 to 8
matrix_1 = np.matrix('0 1 2;3 4 5; 6 7 8')
matrix_1
# %%
# create a 3x3 identiy matrix 
identity_matrix_1 = np.identity(3)
identity_matrix_1
# %%
#use numpy to generate a random number between 0 and 1
random = np.random(0,1)
random
# %%
#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
rand_num = np.random.normal(0,1,25)
rand_num
# %%
matrix = np.matrix(np.arange(0,100)/100)
# %%
#create an array of 20 linearly spaced points between 0 and 1
np.linspace(0,1,20)
# %%
