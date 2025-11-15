import matplotlib.pyplot as plt 
x=["mon","tue","wed","thurs","fri"]
y=[4,3,7,5,6]
plt.plot(x,y,color='black', linestyle='--', linewidth=1, marker='o',label='classes data')
plt.title("no.of hours of classes in a day")
plt.xlabel('week days')
plt.ylabel('no.of hours')
plt.legend()
plt.grid(color='blue',linestyle=':',linewidth='1')

plt.ylim(0,8)
plt.yticks([1,2,3,4,5,6,7,8],['h1','h2','h3','h4','h5','h6','h7','h8'])
plt.show()