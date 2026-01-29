import matplotlib.pyplot as plt
import numpy as np
a = 0.3
wc = 5
wk = np.linspace(-15, 15, 500)
A, B, C, D = -1/2, wc/2, -1/2, -wc/2 
impt3 = (A*wk+B)/((wk-wc)**2 + a**2)
impt4 = (C*wk+D)/((wk+wc)**2 + a**2)
fig, ax = plt.subplots()
fig.set_size_inches(120/25.4,80/25.4)
g1, = ax.plot(wk, impt3, 'g-',\
  lw=2 , label=r'$\frac{1}{2}$')
g2, = ax.plot(wk, impt4, 'r-',\
  label=r'$\omega_{\mathrm{k}}$')
# fuer Legende: Komma nach g1 und g2
# nicht vergessen beim Plot-Befehl!
plt.legend(handles=[g1, g2])
plt.xticks(np.arange(-15,15+5,step=5))
plt.yticks(np.arange(-1,1+0.2,step=0.2))
ax.set_xlim([-15,15])
ax.set_ylim([-1,1])
plt.grid()
plt.xlabel('$\\omega$')
plt.ylabel('Imaginaerteil')
plt.subplots_adjust(left=0.17,\
  right=0.97, top=0.97, bottom=0.15)
plt.savefig('universalgrafik.pdf')
