# %%

import numpy as np
import matplotlib.pyplot as mpl
import os
import matplotlib.ticker as tkr 

def func(x, pos): # formatter
  s1 = '{:1.1f}'.format(x)
  s2 = s1.replace('.',',')
  return s2
y_frmt = tkr.FuncFormatter(func)

print(__file__) # ganzer Pfad
# Nur Dateiname (programm.py):
fn = os.path.basename(__file__)



a = 2
t0 = 0
t1 = 20
t2 = 20
vmax = a * t1
tphase1 = np.linspace(t0,t1,250)
tphase2 = np.linspace(0,t2-t1,250)
fig, axs = mpl.subplots(4)
fig.set_size_inches(70/25.4,150/25.4)

axs[0].set_ylabel('Position (m)')
gxphase1, = axs[0].plot(tphase1, 1/2*a*tphase1**2, 'r-', label='besch')
axs[0].set_xlim([0,t2])
axs[0].set_xticklabels([])
axs[0].set_ylim([0,400])
axs[0].yaxis.set_label_coords(-0.2, 0.5)

axs[1].set_ylabel('Geschw. (m/s)')
gvphase1, = axs[1].plot(tphase1, a*tphase1, 'r-')
axs[1].set_xlim([0,t2])
axs[1].set_ylim([0,40])
axs[1].set_xticklabels([])
axs[1].yaxis.set_label_coords(-0.2, 0.5)


axs[2].set_ylabel('Beschl. $\mathrm{(m/s^2)}$')
gaphase1, = axs[2].plot(tphase1, a+0*tphase1, 'r-')
axs[2].set_xlim([0,t2])
axs[2].set_ylim([0,4])
axs[2].set_xticklabels([])
axs[2].yaxis.set_label_coords(-0.2, 0.5)

axs[3].set_ylabel('Ruck $\mathrm{(m/s^3)}$')
gjphase1, = axs[3].plot(tphase1, 0+0*tphase1, 'r-',zorder=10, linewidth=3)
axs[3].set_xlim([0,t2])
axs[3].set_ylim([0,2])
axs[3].yaxis.set_label_coords(-0.2, 0.5)
axs[3].yaxis.set_major_formatter(y_frmt)

#axs[0].legend(handles=[gnum, gana])
fig.tight_layout(pad=0.0)
axs[0].grid()
axs[1].grid()
axs[2].grid()
axs[3].grid()


axs[3].set_xlabel('Zeit (s)')
mpl.subplots_adjust(left=0.22, right=0.965, top=0.985, bottom=0.075,
  wspace=0.1, hspace=0.10)
fig.show()

fig.savefig(fn[:-3] + '.pdf')

# %%
z = 15/((20-13)**2
         + 7**2)
print(z)