import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize= (10,5))
x=[1,2,3,4]
y=[20,15,32,12]
ax[0].plot(x,y)
ax[0].set_title('line plot')

ax[1].bar(x,y)
ax[1].set_title('bar graph')

plt.show()
