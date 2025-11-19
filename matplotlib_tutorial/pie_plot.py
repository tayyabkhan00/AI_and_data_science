import matplotlib.pyplot as plt

#x=[10,25,67,54]
#y=['python','java','c++','ruby']
#c=['r','g','b','y']
#ex=[0.1,0,0,0]#explode is used to separate the slice from the pie
#plt.pie(x,labels=y,colors=c,autopct="%0.1f%%",shadow=True,explode=ex,,counterclock=False)
#plt.pie(x,labels=y,colors=c,explode=ex,autopct="%0.1f%%",startangle=180,wedgeprops={"linewidth":4},rotatelabels=False)
#plt.title('Pie chart')
#plt.legend(loc=5)
#plt.show()
#autopct is used to show the percentage on the pie

x=[10,25,67,54]
y=['python','java','c++','ruby']
x1=[5,15,32,27]
c=['r','g','b','y']
plt.pie(x,labels=y,colors=c,autopct="%0.1f%%")
#plt.pie(x1,labels=y,radius=0.7)
plt.pie([1], colors=['w'], radius=0.6)#[1] is used to create a white circle in the center
plt.show()