import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,3,1,4,6,5]
plt.plot(x,y)
plt.fill_between(x=[2,4],y1=2,y2=4)
plt.show()