#%%
#import numpy as np
import numpy as np 
# %%
#create an array of 10 zeros
np.zeros(10)
#%%
#create an array of 10 ones
np.ones(10)
# %%
# create an array of 10 fives
np.ones(10)*5
# %%
# np.array[10:51] WRONG BELOW IS THE CORRECT METHOD
np.arange(10,51)
# %%
#Create an array of all the even integers from 10 to 50
np.arange(10,51,2)
# %%
# Create a 3x3 matrix with values ranging from 0 to 8
# np.matrix(0,8) THIS IS INCORRECT BELOW IS THE CORRECT METHOD
np.arange(9).reshape(3,3)
# %%
#createa a 3x3 identity matrix
#COMPLETELY FORGOT WHAT AN IDENTITY MATRIX IS
np.eye(3)
# %%
# np.random(0,1) THIS IS INCORRECT BELOW IS THE CORRECT METHOD
np.random.rand(1)
# %%
# np.arange(25).rand() THIS IS INCORRECT BELOW IS THE CORRECT METHOD
np.random.randn(25)
# %%
# np.arange(0,1)/100 THIS IS INCORRECT BELOW IS THE CORRECT METHOD 
np.arange(1,101).reshape(10,10)/100
# %%
# Create an array of 20 linearly spaced points between 0 and 1:
#I DONT REMEMBER HOW TO DO LINEARLY SPACED POINTS
np.linspace(0,1,20)

# %%
mat = np.arange(1,26).reshape(5,5)
mat
# %%
# mat[13:] THIS IS INCORRECT GO WATCH THE SOLUTIONS VIDEO FOR THIS
mat[2:,1:]
# %%
# mat[0:3,1] THIS IS INCORRECT LOOKAT VIDEO EXPLANATION FOR THIS
mat[:3,1:2]
# %%
