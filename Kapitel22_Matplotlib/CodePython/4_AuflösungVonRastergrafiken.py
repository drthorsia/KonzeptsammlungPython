# 22.4 Auflösung von Rastergrafiken

import matplotlib.pyplot as plt 
import numpy as np
import os

x = np.linspace(-15, 15, 150)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von mm im Zoll 
g1, = ax.plot(x, np.sin(x), color="blue", linewidth=2)

plt.savefig('bilddatei.png', dpi=300)
plt.title("Auflösung von Rastergrafiken", fontsize=10, fontweight="bold")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Auflösung von Rastergrafiken.png"), dpi=300, bbox_inches='tight')
plt.show()

