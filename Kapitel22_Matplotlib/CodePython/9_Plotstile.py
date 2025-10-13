# 22.13 Plotstile 

import matplotlib.pyplot as plt 
import numpy as np 
import os

fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', linewidth=2)

fig.set_size_inches(200/25.4 , 150/25.4)
plt.xlabel('$x$')
plt.ylabel('$sin(x)$')
plt.title("Plotstile", fontsize=10, fontweight="bold")
# plt.subplots_adjust(left=0.22, right=0.97, top=0.80, bottom= 0.22)
plt.grid()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Plotstile.png"), dpi=300, bbox_inches='tight')
plt.show()
