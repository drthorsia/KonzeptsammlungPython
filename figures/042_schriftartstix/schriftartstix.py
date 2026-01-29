import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']=\
   'STIXGeneral'
plt.rcParams['mathtext.fontset']=\
   'stix'
x = np.linspace(0, 12, 150)
fig, ax = plt.subplots()
fig.set_size_inches(80/25.4,50/25.4)
g1, = ax.plot(x, np.sin(x))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.subplots_adjust(left=0.22,\
right=0.97, top=0.97, bottom=0.22)
plt.savefig('schriftartstix.pdf')