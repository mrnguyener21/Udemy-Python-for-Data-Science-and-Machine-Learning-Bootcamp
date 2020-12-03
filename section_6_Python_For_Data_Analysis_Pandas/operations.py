#%%
import numpy as np
import pandas as pd 
# %%
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
# %%
#there are three main value methods to find unique value
df['col2'].unique() #returns the unique values
# %%
df['col2'].nunique()#returns the amount of unique values

# %%
df['col2'].value_counts()
# %%
df[df['col1'] > 2]
# %%
df['col1'] > 2
# %%
df[df['col1'] > 2 &( df['col2'] == 444)] 

# %%
def times2(x):
    return x*2
df['col1'].apply(times2)
# %%
