import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
plt.subplot(2,2,1)
plt.plot(x,y)

plt.subplot(2,2,2)
plt.pie([1])

plt.subplot(2,2,3)
x1=[10,20,30,40]
plt.pie(x1)

plt.subplot(2,2,4)
x2=['a','s','d','f','g']
y2=[4,3,2,1,2]
plt.bar(x2,y2)


plt.show()