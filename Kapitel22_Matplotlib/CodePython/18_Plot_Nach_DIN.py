# 22.25 Plot nach DIN

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import rc
import os 
rc('text', usetex=False) 
rc('legend',**{'fontsize':10}) 
t0 = 0.0
t1 = 1.5
steps = 100
xvals = np.linspace(t0,t1,steps)
yvals1 = xvals**2
yvals2 = np.sin(xvals*2*math.pi)
fig = plt.figure()
#Hoehe, Breite und Position des Plot
rect = 0.14, 0.17, 0.84, 0.80 
ax1 = fig.add_axes(rect,frameon=True)
ax1.set_ylim([-2,2]) 
ax1.set_xlim([t0,t1]) 
stromplot = ax1.plot(xvals, yvals1,\
  label="$x^2$",c='b',lw=0.7/0.3527)
sinusplot = ax1.plot(xvals, yvals2,\
  label="$sin(x)$", color = 'b',\
      ls='--', lw=0.7/0.3527)
ax1.set_xlabel('$t$')
ax1.xaxis.set_label_coords(0.55,\
  0.07, transform=fig.transFigure)
ax1.set_ylabel('$i$')
ax1.yaxis.set_label_coords(0.05,\
  0.5, transform=fig.transFigure)
legend=ax1.legend(\
   loc='lower left',shadow=False)
xls = 0.2
xachseneinheit_str = 's'
x=[ax1.get_xlim()[0]+k*xls for k in \
 range(math.floor((ax1.get_xlim()[1]\
 -ax1.get_xlim()[0])*\
            (1.0+1e-12)/xls)+1)]
lbls=[("%.1f"%d).replace('.',',')\
      for d in x]
lbls[-2]=xachseneinheit_str
plt.xticks(x,lbls)
# Y-Achse:
yachseneinheit_str = 'A'
yls = 0.5
y=[ax1.get_ylim()[0]+k*yls for k in\
 range(math.floor((ax1.get_ylim()[1]\
 -ax1.get_ylim()[0])*\
                  (1.0+1e-12)/yls)+1)]
lblsy=[("%.1f"%d).replace('.',',')\
       for d in y]
lblsy[-2]=yachseneinheit_str
w35=0.35/0.3527
w18=0.18/0.3527
plt.yticks(y,lblsy)
ax1.spines['top'].set_color('none')
ax1.spines['right'].set_color('none')
ax1.spines['bottom'].\
    set_position('zero')
ax1.spines['left'].set_linewidth(w35)
ax1.spines['bottom'].\
    set_linewidth(w35)
print(ax1.xaxis.get_ticks_position())
ax1.xaxis.set_ticks_position('bottom')
ax1.grid(True,which='both',\
  axis='x',c='k',ls='-',lw=w18)
ax1.grid(True,which='both',\
  axis='y',c='k',ls='-',lw=w18)
fig.set_size_inches(100/25.4, 63/25.4)

dstaxtxpt=fig.get_size_inches()[1]*\
  25.4*rect[3]/0.3527*(0-\
  ax1.get_ylim()[0])/\
 (ax1.get_ylim()[1]-\
  ax1.get_ylim()[0])+2
ax1.tick_params(axis='x',\
        which='major', pad=dstaxtxpt)
# Achsenpfeil X:
b_mm=math.tan(7.5*math.pi/180)*20*0.35
arrowlen_mm = 12.0
deltax_frac = arrowlen_mm /\
    (fig.get_size_inches()[0]*25.4)
arrowfrac = 10*0.35/arrowlen_mm
ybf = 0.048
xbf = 0.57
ax1.annotate('',\
  xy=(xbf+deltax_frac,ybf),\
  xycoords='figure fraction',\
  xytext=(xbf,ybf),\
  textcoords='figure fraction',\
  arrowprops=dict(width=w35,\
   facecolor='black',\
  edgecolor= 'none', \
  headwidth=b_mm/0.3527))
# Achsenpfeil Y:
deltay_frac = arrowlen_mm /\
    (fig.get_size_inches()[1]*25.4)
ybyf = 0.52
xbyf = 0.03
ax1.annotate('',\
  xy=(xbyf,ybyf+deltay_frac), \
  xycoords='figure fraction',\
  xytext=(xbyf,ybyf),\
  textcoords='figure fraction',\
  arrowprops=dict(width=w35,\
  facecolor='black',\
  edgecolor= 'none', \
  headwidth=b_mm/0.3527))

plt.title("Plot nach DIN", fontsize=10, fontweight="bold")
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Plot nach DIN.png"), dpi=300, bbox_inches='tight')
plt.show()
