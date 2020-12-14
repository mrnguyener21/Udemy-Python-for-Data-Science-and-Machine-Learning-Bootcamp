#%%
import seaborn as sns 
tips = sns.load_dataset('tips')
tips.head()
# %%
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
# %%
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])

# %%
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'], scatter_kws={'s':100})

# %%
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
# %%
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')

# %%
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',row='time', hue='sex')

# %%
sns.lmplot(x='total_bill',y='tip',data=tips,col='day', hue='sex')

# %%
sns.lmplot(x='total_bill',y='tip',data=tips,col='day', hue='sex', aspect=0.6, size = 8)

# %%
