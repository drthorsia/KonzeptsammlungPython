import matplotlib.pyplot as plt
import os

t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig, ax = plt.subplots() # 1 Reihe, Zwei Spalten

# Verschiebung der Achsenbeschriftungen A mit labelpad
p1 = ax.plot(t, y, color="blue", linewidth=2)
ax.set_xlabel('$xlbl$', labelpad=0)
ax.set_ylabel('$ylbl$', labelpad=0)
ax.set_title("Verschiebung der Achsenbeschriftungen A", fontsize=10, fontweight="bold")
ax.grid(True)
fig.set_size_inches(102.4/25.4 , 76.8/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende 
plt.savefig("Verschiebung_der_Achsenbeschriftung_A.pdf")
