# 22.15 Höhen-Breitenverhältnis 

import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color="blue", linewidth=2)
ax.set_aspect('equal')
fig.set_size_inches(200/25.4 , 150/25.4)

plt.xlabel('$x$')
plt.ylabel('$sin(x)$')
plt.title("Höhen-Breitenverhältnis", fontsize=10, fontweight="bold")
plt.grid()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Höhen-Breitenverhältnis.png"), dpi=300, bbox_inches='tight')
plt.show()
