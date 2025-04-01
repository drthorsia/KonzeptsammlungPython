# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:26:51 2021

@author: thor
"""


import numpy as np
import matplotlib.pyplot as plt
fig, ax= plt.subplots()
fig.set_size_inches(50/25.4, 50/25.4)
xorig=np.linspace(0, 0.999, 50)
x=np.append([1, 0], xorig)
y=np.append([0, 0], np.sqrt(1-xorig**2))
ax.fill(x,y, fill=False, hatch='\\')
plt.subplots_adjust(left=0.22, right=0.97,\
                    top=0.97, bottom=0.22)
ax.set_aspect('equal')
fig.show()
plt.savefig('viertelkreis.pdf')
plt.savefig('viertelkreis.png', dpi=300)

#ax.add_patch(Polygon(np.c_[x,y]))
