import matplotlib.pyplot as plt
import numpy as np

#x=[10,20,30,40,50,60,70,130]
#plt.boxplot(x,
#             notch=True,
#             vert=False,
#             widths=0.5
 #             labels=['python'],
   #           patch_artist=True,
   #           showmeans=True,
#             whis=2,
#             sym='g+'            
#           )
#plt.show()

x=[10,20,30,40,50,60,70]
x1=[10,20,30,40,20,30,50]
y=[x,x1]
plt.boxplot(y,labels=['python','java'])
plt.legend()
plt.show()
