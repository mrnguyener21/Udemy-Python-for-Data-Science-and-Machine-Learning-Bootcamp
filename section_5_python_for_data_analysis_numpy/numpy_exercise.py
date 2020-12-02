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
# matrix_1 = np.matrix('0 1 2;3 4 5; 6 7 8') my solution below is the books solution
matrix_1 = np.arange(9).reshape(3,3)
matrix_1
# %%
# create a 3x3 identiy matrix 
identity_matrix_1 = np.eye(3)
identity_matrix_1
# %%
#use numpy to generate a random number between 0 and 1
random = np.random(0,1)
random
# %%
#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
rand_num = np.random.randn(25)
rand_num
# %%
matrix = np.arange(1,101).reshape(10,10)/100
matrix
# %%
#create an array of 20 linearly spaced points between 0 and 1
np.linspace(0,1,20)
# %%
matrix = np.matrix('12 13 14 15; 17 18 19 20; 22 23 24 25')
matrix
# %%
matrix = np.matrix('2;7;12')
matrix
# %%
arr = np.arange(21,26)
arr
# %%
matrix = np.matrix('16 17 18 19 20 ; 21 22 23 24 25')
matrix

# %%
