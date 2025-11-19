import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[1,3,4,2,5,6]
plt.step(x,y,label='python',marker="o")
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc=2)
plt.show()
