import matplotlib.pyplot as plt
import os

t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig, ax = plt.subplots() # 1 Reihe, Zwei Spalten

t2 = [k for k in range(10)]
y2 = [1/(k+1) for k in t]
p2 = ax.plot(t2, y2, color="blue", linewidth=2)
ax.set_xlabel('$xlbl$')
ax.set_ylabel('$ylbl$', rotation=0, ha='left') # Rotation = drehung in Grad, ha = horizontal aligment (Ausrichtung)
ax.xaxis.set_label_coords(0.95, 0.45)
ax.yaxis.set_label_coords(0.28, 0.95)
ax.set_title("Verschiebung der Achsenbeschriftungen B", fontsize=10, fontweight="bold")
ax.grid(True)

fig.set_size_inches(102.4/25.4 , 76.8/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende 
plt.savefig("Verschiebung_der_Achsenbeschriftungen_B.pdf")
