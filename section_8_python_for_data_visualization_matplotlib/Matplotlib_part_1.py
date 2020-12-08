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
#here the plot function is used to create a basic graph with the function method
plt.plot(x,y)
# %%
#created a basic graph along with a label for the x and y axis and title for the plot with the functional method
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
# %%
#here we created two sub smaller charts within the main chart with their own graph with the functional method
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
# %%
#OBJECT ORIENTED METHOD(USE THIS METHOD)
#here we created a graph with x and y axes along with labeling them and giving a title to the chart(this is done using object oriented method)
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('Title')
# %%
#here we created a graph and a sub graph. The subgraph and large graph is determined on the size of the two graphs. Here axes1 have larger axes than axes 2 so it is the larger graph
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('larger plot')

axes2.plot(y,x)
axes2.set_title('smaller plot')
# %%
