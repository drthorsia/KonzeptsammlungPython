# 22.29 Logarithmische Plots

import matplotlib.pyplot as plt
import numpy as np
import os

x = np.logspace(0.1, 2, 400) # x von 10^0.1 bis 10^2
y = np.sqrt(x)

fig, (ax1, ax2) = plt.subplots(1, 2) # eine Reihe, Zwei Spalten 

# Halblogarithmische Plots(Semi-Log-Diagramm)

ax1.semilogx(x, y, color="blue", linewidth=2) # x-Achse logarithmisch
ax1.set_xlabel('$xlog$')
ax1.set_ylabel('$ylinear$')
ax1.set_title("Halblogarithmischer Plot", fontsize=10, fontweight="bold")
ax1.grid(True, which="both") # grid on both axis 

# Doppeltlogarithmische Plots

ax2.loglog(x, y, color="blue", linewidth=2) # beide Achsen logarithmisch
ax2.set_xlabel('$xlog$')
ax2.set_ylabel('$ylog$')
ax2.set_title("Doppeltlogarithmischer Plot", fontsize=10, fontweight="bold")
ax2.grid(True, which="both")

fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Halb und doppeltlogarithmische Plots.png"), dpi=300, bbox_inches='tight')
plt.show()
