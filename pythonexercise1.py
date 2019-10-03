# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:23:31 2019

@author: 2169099g
"""

import numpy as np
import matplotlib.pylab as plt


pi = np.pi

final_result = 2*pi

step = 8000

c = final_result/step

d = np.arange(0,final_result,c)

print(d)

sin_200x = np.sin(d*200)

plt.plot(d, sin_200x)
plt.xlabel('Angle[Rad]')
plt.ylabel('sin[200x]')
plt.axis('auto')
plt.show()

y=np.cos()