import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color="blue", linewidth=2)
ax.set_aspect('equal') # Achsen gleich skaliert
fig.set_size_inches(200/25.4 , 150/25.4)

plt.xlabel('$x$')
plt.ylabel('$sin(x)$')
plt.title("Höhen-Breitenverhältnis", fontsize=10, fontweight="bold")
plt.grid()
plt.savefig("Hoehen-Breitenverhaeltnis.png", dpi=300, bbox_inches='tight')
plt.show()
