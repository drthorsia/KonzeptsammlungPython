# 22.7 Achsenzahlen verschieben

import matplotlib.pyplot as plt
import os

t = [k for k in range(10)]
y = [1/(k+1) for k in t]

fig, (ax1, ax2) = plt.subplots(1, 2) # 1 Reihe, Zwei Spalten 

# Erstes Bild ohne Achsenzahlen Verschiebeung 
p1 = ax1.plot(t, y, color="blue", linewidth=2)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title("Achsenzahlen nicht verschoben", fontsize=10, fontweight="bold")
ax1.grid(True)

# Zweites Bild mit Achsenzahlen Verschiebung 
p2 = ax2.plot(t, y, color="blue", linewidth=2)
ax2.xaxis.set_tick_params(pad=-15) 
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y$')
ax2.set_title("Achsenzahlen verschoben", fontsize=10, fontweight="bold")
ax2.grid(True)

fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Achsenzahlen verschieben.png"), dpi=300, bbox_inches='tight')
plt.show()

