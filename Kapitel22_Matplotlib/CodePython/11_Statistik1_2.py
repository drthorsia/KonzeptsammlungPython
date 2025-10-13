
import matplotlib.pyplot as plt 
import numpy as np
import os

# Gemeinsame Zufallsdaten
Nx = 3000000
x = np.random.randn(Nx)

# Figur mit zwei Diagrammen (nebeneinander)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 

# 22.16 Statistik 
n, bins, patches = ax1.hist(
    x=x, bins=np.arange(-2.5, 2.75, 0.25),
    color='#0504aa', alpha=0.7, rwidth=0.85
)
ax1.grid(axis='y', alpha=0.75)
ax1.set_xlabel('$Value$')
ax1.set_ylabel('$Frequency$')
ax1.set_title('Normalverteilten Zufallszahlen')
ax1.title.set_fontsize(10)
ax1.title.set_fontweight('bold')

maxfreq = n.max()
ax1.set_ylim(ymax=np.ceil(maxfreq / 10)*10 if maxfreq % 10 else maxfreq + 10)

# 22.17 Statistik 2
grosse = 3
chiv = np.ones(Nx//grosse)
for k in range(Nx//grosse):
    for m in range(grosse):
        chiv[k] = chiv[k] + x[k*grosse + m]**2

n2, bins2, patches2 = ax2.hist(
    x=chiv, bins=np.arange(0, 15, 0.1),
    color='#0504aa', alpha=0.7, rwidth=1.0
)
ax2.grid(axis='y', alpha=0.75)
ax2.set_xlabel('$Value$')
ax2.set_ylabel('$Frequency$')
ax2.set_title('Berechneten X^2-verteilten Werte')
ax2.title.set_fontsize(10)
ax2.title.set_fontweight('bold')

maxf = n2.max()
ax2.set_ylim(ymax=np.ceil(maxf / 10)*10 if maxf % 10 else maxf + 10)

# Gemeinsamer Titel
fig.suptitle("Statistik", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Statistik.png"), dpi=300, bbox_inches='tight')
plt.show()

'''
import matplotlib.pyplot as plt 
import numpy as np


Nx = 30000000
x = np.random.randn(Nx)
# hist, bin_edges = np.histogram(x)
n, bins, patches = plt.hist(x=x, bins=np.arange(-2.5,2.75,0.25), color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My_Very_Own_Histogram')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10)*10 if maxfreq % 10 \
         else maxfreq + 10)
plt.show()



# 22.17 Statistik 2

grosse = 3
chiv = np.ones(Nx//grosse)
for k in range(Nx//grosse):
    for m in range(grosse):
        chiv[k] = chiv[k] + x[k*grosse + m]**2

hist, bin_edges = np.histogram(chiv)
n, bins, patches = plt.hist(x=chiv, bins=np.arange(0,15,0.1), color='#0504aa', alpha=0.7, rwidth=1.0)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My_very_Own_Histogram')
maxf = n.max()
# Set a clean upper y-axis limit
plt.ylim(ymax=np.ceil(maxf / 10) * 10 if maxf % 10 else maxf + 10)'''
