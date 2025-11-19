import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
area1=[2,4,5,3,1,3]
area2=[3,2,3,4,3,2]
area3=[3,2,3,4,5,2]
l=['area1','area2','area3']
plt.stackplot(x,area1,area2,area3,labels=l,
              baseline="wiggle")
plt.legend(loc=2)
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.show()
