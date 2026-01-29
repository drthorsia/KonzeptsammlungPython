import matplotlib.pyplot as plt 
import numpy as np
R = 100
xo = np.linspace(0, 0.999*R, 50)
x = np.append([R,0], xo)
y = np.append([0,0], np.sqrt(R**2-xo**2))
fig, ax = plt.subplots()
fig.set_size_inches(64/25.4, 48/25.4)
ax.fill(x,y, fill=False, hatch='\\')
ax.set_aspect('equal')
plt.subplots_adjust(left=0.12,\
  right=0.99, top=0.97, bottom=0.15)
plt.title("Schraffierte Flächen", fontsize=10, fontweight="bold")
plt.savefig("SchraffierteFlaechen.pdf")
plt.show()
