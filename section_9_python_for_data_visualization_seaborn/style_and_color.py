#%%
import seaborn as sns 
tips = sns.load_dataset('tips')
tips.head()
# %%
sns.countplot(x='sex',data=tips)
# %%
sns.set_style('white')
sns.countplot(x='sex',data=tips)

# %%
sns.set_style('ticks')
sns.countplot(x='sex',data=tips)
# %%
sns.set_style('darkgrid')
sns.countplot(x='sex',data=tips)
# %%
sns.set_style('ticks')
sns.countplot(x='sex',data=tips)
sns.despine()
# %%
