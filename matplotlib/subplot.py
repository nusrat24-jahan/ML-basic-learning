#writing the function for the subplot
import matplotlib.pyplot as plt 
x=[1,2,3,4]
y=[20,15,32,12]
plt.subplot(1,2,1)
plt.plot(x,y,color='pink',label='line_chart',)
plt.title('line chart')
plt.legend()

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar chart')

plt.tight_layout()

plt.show()