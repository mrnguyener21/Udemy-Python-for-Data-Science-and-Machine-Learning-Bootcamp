#%%
import numpy as np
import pandas as pd 

# %%
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df
# %%
df.dropna()#drop ROWS with Nan values
# %%
df.dropna(axis=1)#drop COLUMNS with NaN values
# %%
df.dropna(thresh=2) #will keep the row or column if it has at least that many NaN to reach the threshold
# %%
df.fillna(value = 'Fill Value')#this allows us to fill the NaN cells with a value
# %%
df['A'].fillna(value=df['A'].mean())#in this ex, we are filling the NaN values in column A with the mean of Column A
# %%
