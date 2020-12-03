#%%
import numpy as np
import pandas as pd 

# %%
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
# %%
df = pd.DataFrame(data)
df
# %%
#we can't do groupby with strings
byComp = df.groupby('Company') # here we are grouping by the Company column which  we then can start using aggregate functions on
byComp.mean()
# %%
df.groupby('Company').sum().loc['FB']
# %%
df.groupby('Company').count()
# %%
df.groupby('Company').max()

# %%
df.groupby('Company').describe() #gives you all the info
# %%
df.groupby('Company').describe().transpose() #the transpose just changes the view format of the table