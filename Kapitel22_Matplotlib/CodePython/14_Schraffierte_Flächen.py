# 22.21 Schraffierte Flächen

import matplotlib.pyplot as plt 
import numpy as np
import os

xo = np.linspace(0, 0.999, 50)
x = np.append([1,0], xo)
y = np.append([0,0], np.sqrt(1-xo**2))
fig, ax = plt.subplots()

fig.set_size_inches(200/25.4, 150/25.4)
ax.fill(x,y, fill=False, hatch='\\')
ax.set_aspect('equal')

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Schraffierte Flächen", fontsize=10, fontweight="bold")
# plt.subplots_adjust(left = 0.22, right = 0.97, bottom = 0.22)
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Schraffierte Flächen.png"), dpi=300, bbox_inches='tight')
plt.show()
