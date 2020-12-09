#%%
#this section is literally just making the graph prettier. kinda like css
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color='orange',lw=1,alpha=0.8,ls='-',marker='o', markersize=10, markerfacecolor='green',markeredgewidth=3,markeredgecolor='black')
# %%
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color='orange',lw=2,ls='-')
ax.set_xlim([0,1])
ax.set_ylim([0,2])
# %%
