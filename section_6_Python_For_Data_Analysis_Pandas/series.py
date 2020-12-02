#%%
import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
labels
# %%
pd.Series(data = my_data)
#a series will show the index and you can label the indexes as well as shown below
# %%
pd.Series(data=my_data,index=labels)
# %%
#we can also pass a numpy array
pd.Series(arr,labels)

# %%
# we can also pass our dicionary
pd.Series(d)

# %%
pd.Series(data=labels)
# %%
pd.Series(data=[sum,print,len])
# %%
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser1
# %%
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
ser2
# %%
# doing this can get the data correlated to it 
ser1['USA']
# %%
ser3 = pd.Series(data=labels)
ser3
# %%
ser3[0]
# %%
#added series together will addd based on matching indexes
ser1 + ser2
# %%
