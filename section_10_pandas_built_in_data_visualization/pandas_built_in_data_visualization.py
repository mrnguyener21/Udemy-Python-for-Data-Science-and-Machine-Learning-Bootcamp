#%%
import numpy as np 
import seaborn as sns 
import pandas as pd 

# %%
df1 = pd.read_csv('df1.csv',index_col=0)
# %%
df1.head()
# %%
df2 = pd.read_csv('df2.csv')
df2.head()
#%%
df1['A'].hist(bins=30)
# %%
df1['A'].plot(kind='hist', bins=30)
# %%
#use this method
df1['A'].plot.hist()
# %%
df2.plot.area(alpha=0.5)
# %%
df2.plot.bar()
# %%
df1.plot.line(x = df1.index, y = 'B')
# %%
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')
# %%
df1.plot.scatter(x='A',y='B',s=df1['C']*40)

# %%
df2.plot.box()
# %%
df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
df
# %%
df.plot.hexbin(x='a',y='b',gridsize=25)
# %%
df2['a'].plot.kde()
# %%
