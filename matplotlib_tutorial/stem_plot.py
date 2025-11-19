import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[2,3,5,3,3,4]
#plt.stem(x,y,
#      linefmt=':',
#      markerfmt='r+',
#      bottom=5,
#      basefmt='g', 
#      orientation='horizontal')
plt.stem(x,y,label='python')
plt.legend()
plt.show()