#%%
import matplotlib.pyplot as plt
import numpy as np
# %%
x = np.linspace(0,5,11)
y = x ** 2
x
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('larger plot')

axes2.plot(y,x)
axes2.set_title('smaller plot')
# %%
fig,axes = plt.subplots(nrows =1 , ncols =2)
# axes.plot(x,y)
# for current_ax in axes:
#     current_ax.plot(x,y)
axes[0].plot(x,y)
axes[0].set_title('first plot')
axes[1].plot(y,x)
axes[1].set_title('second plot')

plt.tight_layout()
# %%
fig = plt.figure(figsize = (8,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
# %%
fig,axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8,2))
axes[0].plot(x,y)
axes[1].plot(x,y)
plt.tight_layout()
# %%
# fig.savefig('my_picture.png',dpi = 200)
# %%
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = 'X SQUARED')
ax.plot(x,x**3, label = 'X CUBED')

ax.legend(loc=0)
# %%
