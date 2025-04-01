#%%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tkr 
import os
from math import pi

plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['pdf.fonttype'] = 42

def func(x, pos): # Komma Statt Punkt als Dezimaltrennzeichen
  s1 = '{:1.1f}'.format(x)
  s2 = s1.replace('.',',')
  return s2
ax_frmt = tkr.FuncFormatter(func)

def bilininterp(x, y, x0, x1, y0, y1, j_LU, j_LO, j_RU, j_RO):
    return(1/((y1-y0)*(x1-x0)) * (((x1-x)*j)))




#%%

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import clear_output
import matplotlib

phi00 = 1
phi01 = 2
phi10 = 3
phi11 = 7
x0 = 1
x1 = 5
y0 = 1
y1 = 5

def phixy(xp, yp):
    retval = 1/((y1-y0)*(x1-x0)) * (((x1-xp)*phi00 + (xp-x0)*phi10) 
    * (y1-yp) + ((x1-xp)*phi01 + (xp-x0)*phi11) * (yp-y0))
    return(retval)

def harryplotter(xpar=2, ypar=3):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import cm
    xv=np.linspace(x0,x1,15)
    yv=np.linspace(y0,y1,15)
    Mx,My=np.meshgrid(xv,yv)
    phi = phixy(Mx,My)
    plt, ax = plt.subplots() 
    plt.set_size_inches(120/25.4,80/25.4)
    surf = ax.contourf(Mx, My, phi, 100, cmap=cm.gray)
    plt.colorbar(surf, ax=ax)
    ax.set_xlim([0,6])
    ax.set_ylim([0,6])
    ax.plot([xpar],[y1],'ko')
    ax.plot([x1, x1, x0, x0],[y1, y0, y1, y0], 'ko', marker=matplotlib.markers.MarkerStyle('o', fillstyle='none'), color='black')
    ax.plot([xpar],[y0],'ko')
    ax.plot([xpar],[ypar],'ko')
    ax.text(x1+0.1, y1+0.1, '$\\varphi_\mathrm{RO}$')
    ax.text(x0-0.2, y1+0.1, '$\\varphi_\mathrm{LO}$', ha='right')
    ax.text(x0-0.2, y0+0.1, '$\\varphi_\mathrm{LU}$', ha='right')
    ax.text(x1+0.1, y0+0.1, '$\\varphi_\mathrm{RU}$')
    ax.text(xpar, 0.1, '$x$', ha='center')
    ax.text(0.1, ypar, '$y$', va='center')
    print("Funktionswert: {0:1.2f}".format(phixy(xpar,ypar)))
    plt.show()

harryplotter()
