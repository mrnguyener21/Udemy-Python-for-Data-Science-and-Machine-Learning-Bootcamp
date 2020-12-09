#%%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
# %%
#ex 1
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
# %%
#ex 2
fig= plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
# %%
#ex 3
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')


ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)

# %%
#ex 4
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,2))
axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
# %%
