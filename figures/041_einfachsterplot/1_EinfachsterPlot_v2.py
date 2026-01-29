import matplotlib.pyplot as plt # Erstellung von Grafiken
import numpy as np # Rechnen und Datenverarbeitung
import os

t = [k for k in range(0, round(70/0.2))]
tbl = [1/(1+k*0.2) for k in t]

plt.plot(t, tbl, color="blue", linewidth=2)
plt.title("Einsfachster Plot", fontsize=10, fontweight="bold")
plt.xlabel('$t$')
plt.ylabel('$tbl$')
plt.grid()
plt.savefig("EinfachsterPlot.png", dpi=300, bbox_inches='tight')
# bbox_inches='tight' Entfernt unnötigen Leerraum um das Diagramm
# dpi: Auflösung des Bildes in Punkten pro Zoll (300 für hohe Qualität)
