#%%
import numpy as np
arr = np.arange(0,11)
# %%
arr[8]
# %%
arr[1:5]
# %%
arr[0:5]
# %%
arr[:6]
# %%
arr[5:]
# %%
arr[0:5] = 100
# %%
arr
# %%
arr = np.arange(0,11)
arr
# %%
slice_of_arr = arr[0:6]
slice_of_arr
# %%
arr_copy = arr.copy() #you need to use the copy function because slice_of_arr currently is just a view, so changes to it will change the orignial array as well

# %%
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d
# %%
