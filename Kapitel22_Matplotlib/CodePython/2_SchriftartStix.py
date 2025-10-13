# 22.2 Schriftart Stix

import matplotlib.pyplot as plt # Für Erzeugung von Diagramme und Darstellungen in verschiedenen Formaten 
import numpy as np
import os

plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['mathtext.fontset'] = 'stix'
   
x = np.linspace(0, 12, 150)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
g1 = ax.plot(x, np.sin(x), color="blue", linewidth=2)

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Schriftart Stix", fontsize=10, fontweight="bold")
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Schriftart Stix.png"), dpi=300, bbox_inches='tight')
plt.show()