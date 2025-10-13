# 22.22 Gefüllte Plots

import matplotlib.pyplot as plt 
import numpy as np
import os

fig, ax = plt.subplots()
xorig = np.linspace(0, 1 ,30)
x = np.append([0], xorig)
y = np.append([0], np.sqrt(1-xorig**2))
ax.fill(x, y)
ax.plot(x, y, 'k-')

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Gefüllte Plots", fontsize=10, fontweight="bold")
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Gefüllte Plots.png"), dpi=300, bbox_inches='tight')
plt.show()
