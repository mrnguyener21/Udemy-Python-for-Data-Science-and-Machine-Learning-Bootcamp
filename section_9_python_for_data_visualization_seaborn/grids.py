#%%
import matplotlib.pyplot as plt 
import seaborn as sns 
iris = sns.load_dataset('iris')
iris.head()
# %%
# %%
g = sns.PairGrid(iris)
g
# %%
g.map(plt.scatter)
# %%
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

# %%
tips = sns.load_dataset('tips')
tips.head()
# %%
g = sns.FacetGrid(data=tips,col='time',row='smoker')
# %%
g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')

# %%
g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(plt.scatter,'total_bill','tip')
# %%
