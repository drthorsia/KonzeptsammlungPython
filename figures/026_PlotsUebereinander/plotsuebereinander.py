# %%

import numpy as np
import matplotlib.pyplot as mpl
t = np.linspace(0,10,75)
fig, axs = mpl.subplots(3)
fig.set_size_inches(70/25.4,125/25.4)
axs[0].set_ylabel('Position (m)')
gxphase1, = axs[0].plot(t, 1/2*t**2, 'r-', label='besch')
axs[1].set_ylabel('Geschw. (m/s)')
gvphase1, = axs[1].plot(t, t, 'r-')
axs[2].set_ylabel('Beschl. $\mathrm{(m/s^2)}$')
gaphase1, = axs[2].plot(t, 1+0*t, 'r-')

axs[0].grid()
axs[1].grid()
axs[2].grid()

axs[0].set_xlim([0,10])
axs[0].set_xticklabels([])
axs[1].set_xlim([0,10])
axs[1].set_xticklabels([])
axs[2].set_xlim([0,10])
axs[0].set_ylim([0,50])
axs[1].set_ylim([0,10])
axs[2].set_ylim([0,2])

axs[2].set_xlabel('Zeit (s)')
mpl.subplots_adjust(left=0.23, right=0.94, top=0.99, bottom=0.09, wspace=0.1, hspace=0.2)
fig.show()
fig.savefig('x-v-a-diagramm.pdf')

# %%
