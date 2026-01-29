import matplotlib.pyplot as plt 
import numpy as np
import os

# Gemeinsame Zufallsdaten
Nx = 3000000
x = np.random.randn(Nx)

# Figur mit zwei Diagrammen (nebeneinander)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 

# 22.16 Statistik 
n, bins, patches = ax.hist(
    x=x, bins=np.arange(-2.5, 2.75, 0.25),
    color='#0504aa', alpha=0.7, rwidth=0.85
)
ax.grid(axis='y', alpha=0.75)
ax.set_xlabel('$Value$')
ax.set_ylabel('$Frequency$')
ax.set_title('Normalverteilten Zufallszahlen')
ax.title.set_fontsize(10)
ax.title.set_fontweight('bold')

maxfreq = n.max()
ax.set_ylim(ymax=np.ceil(maxfreq / 10)*10 if maxfreq % 10 else maxfreq + 10)

fig.suptitle("Statistik", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("Statistik1.pdf")
plt.show()
