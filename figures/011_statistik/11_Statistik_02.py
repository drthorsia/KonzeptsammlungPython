
import matplotlib.pyplot as plt 
import numpy as np
import os

Nx = 3000000
x = np.random.randn(Nx)

fig, ax2 = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
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
fig.suptitle("Statistik 2", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("Statistik_b.pdf")
plt.show()
