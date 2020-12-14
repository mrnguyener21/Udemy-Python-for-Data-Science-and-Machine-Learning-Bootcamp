#%%
import seaborn as sns 
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
# %%
tc = tips.corr()
tc
# %%
sns.heatmap(tc)
# %%
sns.heatmap(tc,annot=True)

# %%
sns.heatmap(tc,annot=True,cmap='coolwarm')

# %%
flights
# %%
fp = flights.pivot_table(index='month',columns='year',values='passengers')
fp
# %%
sns.heatmap(fp)
# %%
sns.heatmap(fp,cmap='magma')

# %%
sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)

# %%
sns.clustermap(fp, cmap='coolwarm')
# %%
sns.clustermap(fp, cmap='coolwarm',standard_scale=1)

# %%
