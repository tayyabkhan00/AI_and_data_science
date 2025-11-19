import matplotlib.pyplot as plt
import numpy as np

multiple=[2,4,6,8,10,12,14]
no=[1,2,3,4,5,6,7]
c=['r','y','g','b','y','r','b']
s=[50,100,30,40,100,70,100]
no2=[7,6,5,4,3,2,1]
#plt.scatter(multiple,no,color=c,s=s,alpha=0.5,marker='*',edgecolors='b',linewidths=2)  
#alpha is used to set the transparency of the dot
plt.scatter(multiple,no,color=c,s=s,cmap='virdis')
plt.scatter(multiple,no2,color='b',s=s,)
t=plt.colorbar()
t.set_label('colorbar')
plt.xlabel('multiple')
plt.ylabel('no')
plt.title('no')
plt.show()