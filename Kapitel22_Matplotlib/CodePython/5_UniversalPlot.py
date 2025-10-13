# 22.5 Universal-Plot

import matplotlib.pyplot as plt
import numpy as np
import os

a = 0.3
wc = 5
wk = np.linspace(-15, 15, 500)
A, B, C, D = -1/2, wc/2, -1/2, -wc/2
impt3 = (A*wk+B)/((wk-wc)**2 + a**2) # a**2 = a^2
impt4 = (C*wk+D)/((wk-wc)**2 + a**2)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4)
g1, = ax.plot(wk,impt3, 'g-', lw=5, label=r'$\frac{1}{2}$')
g2, = ax.plot(wk,impt4, 'r-', lw=5, label=r'$\omega_{\mathrm{k}}$')

# fuer Legende: Komma nach g1 und g2 nicht vergessen beim Plot-Befehl!
plt.legend(handles=[g1, g2])
plt.xticks(np.arange(-2, 13 , step=1))
ax.set_xlim([-15 , 15])
ax.set_ylim([-1 , 1])
plt.title("Universal-Plot", fontsize=10, fontweight="bold")
plt.grid()
plt.xlabel('$\omega$')
plt.ylabel('$Imaginearteil$')
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Universal-Plot.png"), dpi=300, bbox_inches='tight')
plt.show()

