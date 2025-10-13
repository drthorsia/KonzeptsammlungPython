# 22.18 Verschiebung der Achsenbeschriftungen

import matplotlib.pyplot as plt
import os

t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig, (ax1, ax2) = plt.subplots(1, 2) # 1 Reihe, Zwei Spalten

# Verschiebung der Achsenbeschriftungen A mit labelpad
p1 = ax1.plot(t, y, color="blue", linewidth=2)
ax1.set_xlabel('$xlbl$', labelpad=0)
ax1.set_ylabel('$ylbl$', labelpad=0)
ax1.set_title("Verschiebung der Achsenbeschriftungen A", fontsize=10, fontweight="bold")
ax1.grid(True)


# 22.19 Verschiebung der Achsenbeschriftungen B mit set_label_coords

t2 = [k for k in range(10)]
y2 = [1/(k+1) for k in t]
p2 = ax2.plot(t2, y2, color="blue", linewidth=2)
ax2.set_xlabel('$xlbl$')
ax2.set_ylabel('$ylbl$', rotation=0, ha='left') # Rotation = drehung in Grad, ha = horizontal aligment (Ausrichtung)
ax2.xaxis.set_label_coords(0.95, 0.45)
ax2.yaxis.set_label_coords(0.28, 0.95)
ax2.set_title("Verschiebung der Achsenbeschriftungen B", fontsize=10, fontweight="bold")
ax2.grid(True)

fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Verschiebung der Achsenbeschriftungen.png"), dpi=300, bbox_inches='tight')
plt.show()
