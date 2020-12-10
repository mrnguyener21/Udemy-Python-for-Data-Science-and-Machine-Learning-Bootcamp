#%%
import seaborn as sns 
tips = sns.load_dataset('tips')
tips
# %%
sns.distplot(tips['total_bill'])
# %%
sns.distplot(tips['total_bill'], kde=False)

# %%
sns.distplot(tips['total_bill'], kde=False,bins=30)

# %%
sns.jointplot(x='total_bill',y='tip',data=tips)
# %%
sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')

# %%
sns.pairplot(tips)
# %%
sns.pairplot(tips, hue='sex')

# %%
sns.pairplot(tips, hue='sex',palette='coolwarm')

# %%
sns.rugplot(tips['total_bill'])
# %%
