# 22.24 2D-Flaechenplot

import matplotlib.pyplot as plt 
import numpy as np
import os
from matplotlib import cm 

phi00 = 1
phi01 = 2
phi10 = 3
phi11 = 7
x0 = 1 
x1 = 5
y0 = 1
y1 = 5

def phixy(xp, yp):
    retval = 1/((y1-y0)*(x1-x0)) * (((x1-xp)*phi00 + (xp-x0)*phi10)
    * (y1-yp) + ((x1-xp)*phi01 + (xp-x0)*phi11) * (yp-y0))
    return(retval)

xv = np.linspace(x0, x1 ,15)
yv = np.linspace(y0, y1, 15)
Mx, My = np.meshgrid(xv, yv)
phi = phixy(Mx, My)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4, 150/25.4)
ax.set_title('2D-Flaechenplot')
ax.title.set_fontsize(10)
ax.title.set_fontweight("bold")
surf = ax.contourf(Mx, My, phi, 100, cmap=cm.jet)
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "2D-Flächenplot.png"), dpi=300, bbox_inches='tight')
plt.show()