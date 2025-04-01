import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from matplotlib.ticker import FuncFormatter # Für Dezimaltrennzeichen Komma
from matplotlib import rc #für Schriftart Palatino
rc('font',**{'family':'serif','serif':['Palatino'],'size':10}) #für Schriftart Palatino
rc('text', usetex=True) #für Schriftart Palatino
rc('legend',**{'fontsize':10}) # Für Schriftgröße 10 in der Legende
#Siehe http://stackoverflow.com/questions/12402561/how-to-set-font-size-of-matplotlib -axis-legend
 ## arrowed_spines for plots: https://gist.github.com/joferkington/3845684

def arrowed_spines(ax=None, arrow_length=20, labels=('', ''), arrowprops=None):
    xlabel, ylabel = labels
    if ax is None:
        ax = plt.gca()
    if arrowprops is None:
        arrowprops = dict(arrowstyle='<|-', facecolor='black')

    for i, spine in enumerate(['left', 'bottom']):
        # Set up the annotation parameters
        t = ax.spines[spine].get_transform()
        xy, xycoords = [0.97, 0], ('axes fraction', t)
        xytext, textcoords = [arrow_length, 0], ('offset points', t)
        ha, va = 'left', 'bottom'
        if spine is 'bottom':
            xarrow = ax.annotate(xlabel, xy, xycoords=xycoords, xytext=xytext, textcoords=textcoords,\
                                 ha=ha, va='center', arrowprops=arrowprops)
        else:
            yarrow = ax.annotate(ylabel, xy[::-1], xycoords=xycoords[::-1], xytext=xytext[::-1],\
                                 textcoords=textcoords[::-1], ha='center', va=va, arrowprops=arrowprops)
    return xarrow, yarrow

t0 = 0.0
t1 = 1.2
steps = 100
zeit = np.linspace(t0,t1,steps)
i0 = 0.0
ymin=-5.8
ymax = 5.8
gfxlevel = 0 # 0=überlagerung, 1=beschriftung

fig = plt.figure()
xpart=0.10
rect = xpart, 0.02, 1-xpart-0.06, 0.87
ax1 = fig.add_axes(rect, frameon=True)
ax1.set_ylim([ymin, ymax])
ax1.grid() #toggles grid state http://matplotlib.org/api/axis_api.html
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data',0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))
arrowed_spines(ax1,arrow_length=15) # add arrows to spines

if gfxlevel == 0:
    # strom1
    yvals = [4*math.cos(2*math.pi/1*t) for t in zeit]
    spannungsplot = ax1.plot(zeit , yvals , label="Strom", color = 'r', linewidth=2) #wichtig ist das Komma

    # Strom2
    yvals2 = [3*math.sin(2*math.pi/1*t) for t in zeit]
    stromplot = ax1.plot(zeit, yvals2 , label="Strom", color = 'r', linewidth=2) #wichtig ist das Komma

# Summenstrom
yvals3 = [4*math.cos(2*math.pi/1*t)+3*math.sin(2*math.pi/1*t) for t in zeit]
stromplot = ax1.plot(zeit, yvals3 , label="Strom", color = 'darkred', linewidth=2) #wichtig ist das Komma

# Anmerkungen
if gfxlevel == 0:
    plt.annotate("$i_R(t)$", xy=(0.35, -1.8), xytext=(0.02, -4), arrowprops=dict(arrowstyle="->",facecolor='black'))
    plt.annotate("$i_L(t)$", xy=(0.42, 1.1), xytext=(0.55, 2.7), arrowprops=dict(arrowstyle="->",facecolor='black'))
    plt.annotate("$i(t)$", xy=(0.22, 3.4), xytext=(0.35, 4.0), arrowprops=dict(arrowstyle="->",facecolor='black'))

if gfxlevel == 1:
    # Maximalstrom
    plt.annotate("$\hat{i}$", xy=(0.12, 5), xytext=(-0.11, 4.8), arrowprops=dict(arrowstyle="->", facecolor='black'))

    # Ti
    ax1.arrow(0.1, 5, 0.0, -3.7, head_width=0.02, head_length=0.9, fc='k', ec='k', zorder=40)
    ax1.text(0.1,-1.3,"$-t_i$", color='k', horizontalalignment='center', verticalalignment='top')

    # Periodendauer
    ax1.arrow(0.53, 5.5, -0.37, 0.0, head_width=0.25, head_length=0.04, fc='k', ec='k', zorder=40)
    ax1.arrow(0.67, 5.5, 0.37, 0.0, head_width=0.25, head_length=0.04, fc='k', ec='k', zorder=40)
    ax1.text(0.6,5.5,"$T$", color='k', horizontalalignment='center', verticalalignment='center')
ax1.grid()

# für die Koordinaten siehe http://stackoverflow.com/questions/9290938/how-to-set-my-xlabel -at-the-end-of-xaxis
ax1.set_xlabel('Zeit (s)')
ax1.xaxis.set_label_coords(0.96, 0.18)
ylabel = ax1.set_ylabel('Strom (A)', color='r')
ax1.yaxis.set_label_coords(0.19, 1.0)
#ax1.text(0.08, 4.2, 'Leistung (W)', color='orange')
ylabel.set_rotation(0)
formatter = FuncFormatter(lambda x, pos: ("%.1f"%x).replace(".",",")) # für Dezimaltrennzeichen Komma
ax1.xaxis.set_major_formatter(formatter) # für Dezimaltrennzeichen Komma
#ax1.yaxis.set_major_formatter(formatter) # für Dezimaltrennzeichen Komma
fig.set_size_inches(3.94,2.46) # breite = ~100 mm, seitenverhaeltnis 1,6:1
fig.set_size_inches(58.6/25.4,37/25.4) # breite = ~100 mm, seitenverhaeltnis 1,6:1
plt.savefig('grafik{:d}.svg'.format(gfxlevel),format='svg')
plt.savefig('grafik{:d}.pdf'.format(gfxlevel),format='pdf', transparent=True)
#plt.show()