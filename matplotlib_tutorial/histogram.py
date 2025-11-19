import matplotlib.pyplot as plt
import numpy as np

import random
x=np.random.randint(10,60,(50))
print(x)

no=[19,18,2,4,19,44,49,25,39,22,39,36,50,55,30,27,37,10,13,47,22,38,45,33
,19,58,55,10,47,55,32,54,38,56,31,55,46,54,38,51,29,56,51,18,46,48,21,33
,32,55]
#plt.hist(no,bins="auto",range=(0,100),edgecolor='r',orientation='horizontal',rwidth=0.5,log=True,label='python')
#plt.hist(no,color='b',edgecolor='r',cumulative=-1,bottom=10,align='left',histtype='step')
plt.hist(no,color='b',edgecolor='r',label='python')
plt.title('histogram chart')
plt.xlabel('python')
plt.ylabel('no')
plt.axvline(x=45,color='g',label="line")
plt.legend()
#plt.grid()
plt.show()