import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from matplotlib.ticker import FuncFormatter, MultipleLocator, FormatStrFormatter # Für Dezimaltrennzeichen Komma
from matplotlib import rc #für Schriftart Palatino
rc('font',**{'family':'serif','serif':['Palatino'],'size':10}) #für Schriftart Palatino
rc('text', usetex=True) #für Schriftart Palatino
rc('legend',**{'fontsize':10}) # Für Schriftgröße 10 in der Legende

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

f0 = 1
f1 = 1000
steps = 10
freq = np.logspace(math.log10(f0),math.log10(f1), num=steps)
i0 = 0.0
ampmin=1e-3
ampmax = 10
phimin = -90
phimax = 90
gfxlevel = 0 # 0=überlagerung, 1=beschriftung

fig = plt.figure()
xpart=0.16
rect1 = xpart, 0.57, 1-xpart-0.06, 0.38
ax1 = fig.add_axes(rect1, frameon=True)
rect2 = xpart, 0.05, 1-xpart-0.06, 0.38
ax2 = fig.add_axes(rect2, frameon=True)


# Erster Plot
ax1.set_ylim([ampmin, ampmax])
ax1.grid() #toggles grid state http://matplotlib.org/api/axis_api.html
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
arrowed_spines(ax1,arrow_length=15) # add arrows to spines


# Zweiter Plot
ax2.set_ylim([phimin, phimax])
ax2.grid() #toggles grid state http://matplotlib.org/api/axis_api.html
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.spines['bottom'].set_position(('data',0))
ax2.yaxis.set_ticks_position('left')
arrowed_spines(ax2,arrow_length=15) # add arrows to spines

R=100
C=47e-6
if gfxlevel == 0:
    # strom1
    yvals = [math.sqrt(\
        (1/((R*2*math.pi*f*C)**2 + 1))**2+\
        ((R * 2 * math.pi * f * C) / ((R*2*math.pi*f*C)**2 + 1))**2) for f in freq]
    print(freq)
    spannungsplot = ax1.loglog(freq , yvals , label="Amplituide", color = 'r', linewidth=2) #wichtig ist das Komma

phasevals = [180/math.pi * (math.atan((-R*2*math.pi*f*C)/(1)) - math.atan((0)/((R*2*math.pi*f*C)**2+1))) for f in freq]
phaseplot = ax2.semilogx(freq , phasevals , label="Phase", color = 'r', linewidth=2) #wichtig ist das Komma

ax1.set_xlabel('Frequenz (Hz)')
ax1.xaxis.set_label_coords(0.82, 0.18)

# Y1-Label
ylabel = ax1.set_ylabel("$\\left| \\frac{\\underline{U_\\mathrm{A}}}{\\underline{U_\\mathrm{E}}} \\right|_\mathrm{dB}$", color='k')
ylabel.set_rotation(0)
ax1.yaxis.set_label_coords(0.15, 0.85)

# Achsenbeschriftung X Phasenplot
ax2.set_xlabel('Frequenz (Hz)')
ax2.xaxis.set_label_coords(0.82, 0.32)

# Achsenbeschriftung Y2
achsenbezifferung_y2 = 30
ymajorLocator2 = MultipleLocator(achsenbezifferung_y2) # Argument gibt den Abstand an, zwischen denen ein Tick angegeben wird
ax2.yaxis.set_major_locator(ymajorLocator2)
ax2.text(1.5, 60, '$\\mathrm{arg}\\!\\left( \\frac{\\underline{U_\\mathrm{A}}}{\\underline{U_\\mathrm{E}}} \\right)$', color='k')

fig.set_size_inches(58.6/25.4,74/25.4) # 
plt.savefig('grafik{:d}.pdf'.format(gfxlevel),format='pdf', transparent=True)
