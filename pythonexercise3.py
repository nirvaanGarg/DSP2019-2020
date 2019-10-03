# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:49:24 2019

@author: 2169099g
"""

import numpy as np
import matplotlib.pyplot as plt



fc = 0.5
fm = 10

del_f = abs(fc - fm)

print(type(del_f))

wc = 2*np.pi*fc
wm = 2*np.pi*fm
t = np.linspace(0,2*np.pi,8000)

y = np.cos((wc*t)+(del_f/fm)*np.sin(wm*t))

plt.plot(t,y)
plt.xlabel('Timeframe')
plt.ylabel('freqmod')
plt.axis('auto')
plt.show()

