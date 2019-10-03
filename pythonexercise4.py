# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:46 2019

@author: 2169099g
"""

import numpy as np
import matplotlib.pyplot as plt


a = np.empty(8000,dtype=np.float64)
print(a)

two_pi = 2*np.pi

resultant = two_pi/8000

for b in range(8000):
    a[b] = b*resultant

print(a)

for c in range(201):
    sin200_x = np.sin(c*a)
    

plt.plot(sin200_x)
plt.ylabel('radians')
plt.xlabel('timeframe')
plt.axis('auto')

plt.show()

"""for fc in range(1:10):
    efc = np.zeros(9)
    efc[fc-1]= fc
    for fm in range(0.1:0.9):
        efm= np.zeros(8)
        efm[fm-0.1] = fm"""
        
fc = 10
fm = 0.9        
        
del_f = abs(fc - fm)
wm= 2*np.pi*fm
wc = 2*np.pi*fc



g = np.zeros(2)
for i in range(len(a)) :
    y[i] = np.cos((wc*a[i])+(del_f/fm)*np.sin(wm*a[i]))

plt.plot(y)
plt.xlabel('radians')
plt.ylabel('freqmod')
plt.axis('auto')
plt.show()