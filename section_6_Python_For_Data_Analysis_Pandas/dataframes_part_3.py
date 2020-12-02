#%%
import numpy as np
import pandas as pd 
from numpy.random import randn
np.random.seed(101)
# %%
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)#the multiIndex is what creates an index higharchy in the table

# %%
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df
# %%
df.loc['G1'].loc[1] #here we call the outside index first and then the secondary index
# %%
df.index.names =['Groups','Num'] #how we give names to the index columns
# %%
df.loc['G2'].loc[2]['B']
# %%
df.loc['G1'].loc[1]['B']
# %%
df.xs(1, level='Num')#lets us request data that can belong to different sections
# %%
