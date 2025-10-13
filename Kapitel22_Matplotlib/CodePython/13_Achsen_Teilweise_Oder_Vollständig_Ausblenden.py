# 22.20 Achsen teilweise oder vollständig ausblenden 

import matplotlib.pyplot as plt
import os

t = [k for k in range(10)]
y = [1/(k+1) for k in t]

fig, (ax1, ax2) = plt.subplots(1, 2) # 1 Reihe, Zwei Spalten 

# Erstes Bild Achsen teilweise ausblenden  
p1 = ax1.plot(t, y, color="blue", linewidth=2)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title("Achsen teilweise ausblenden", fontsize=10, fontweight="bold")

ax1.spines['bottom'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.grid(True)

# Zweites Bild Achsen vollstaendig ausblenden
p2 = ax2.plot(t, y, color="blue", linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y$')
ax2.set_title("Achsen vollständig ausblenden", fontsize=10, fontweight="bold")

ax2.spines['top'].set_color('none')
ax2.spines['right'].set_color('none')
ax2.spines['bottom'].set_color('none')
ax2.spines['left'].set_color('none')
ax2.grid(True)

# Alle Achsenteile ausblenden:
plt.axis('off')

fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt für schoene Abstaende 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Achsen teilweise oder vollständig ausblenden.png"), dpi=300, bbox_inches='tight')
plt.show()
