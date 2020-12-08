#%%
import matplotlib.pyplot as plt

# %%
import numpy as np
# %%
x = np.linspace(0,5,11)
y = x ** 2
x
# %%
y
# %%
#FUNCTIONAL METHOD
plt.plot(x,y)
# %%
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
# %%
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
# %%
#OBJECT ORIENTED METHOD(USE THIS METHOD)
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
# %%
