# 22.8 Positionen Hilfsgitterlinien 

import matplotlib.pyplot as plt 
import numpy as np
import os

t = np.linspace(0 ,12 ,100)
y = 4*t**2-3*t+3
fig, ax = plt.subplots()
p1 = ax.plot(t, y, color="blue", linewidth=2)

plt.xticks(np.arange(0 ,12+1 ,step=1))
plt.yticks(np.arange(0, 601 ,step=50))


# 22.9 Beschriftungspfeile

plt.annotate("", xy=(4,200), xytext=(8,200),
             arrowprops=dict(arrowstyle="|-|",
                             linewidth=1.3, color='k', shrinkA=0,
                             shrinkB=0, capstyle='round'))

# 22.10 Beschriftungstext oben in der Mitte setzen

xm = (4 + 8) / 2
ym = (200 + 200) / 2

plt.text(xm, ym + 0.5,
          "Beschriftungspfeile", color= "red",
          ha='center', va='bottom', fontsize=10)


# 22.11 Groeße der Abbildung

fig.set_dpi(150) # Dots per Inch. Anzahl der Bildpunkte (Pixel) pro Zoll


# 22.12 Grenzen der Achsen 

xmin, xmax, ymin, ymax = 0, 14, 0, 605

ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])


plt.title("Positionen Hilfsgitterlinien", fontsize=10, fontweight="bold")
fig.set_size_inches(200/25.4 , 150/25.4)
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.grid()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Positionen Hilfsgitterlinien.png"), dpi=300, bbox_inches='tight')
plt.show()
