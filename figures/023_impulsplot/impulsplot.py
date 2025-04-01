# %%
import matplotlib.pyplot as plt
import numpy as np
xavg = 1.5
xsigma = 0.15
fig, ax = plt.subplots()
fig.set_size_inches(120/25.4,80/25.4)
np.random.seed(0)
x = np.random.normal(xavg, xsigma, 12)
y = 0.0*x+1
ml, sl, bl = ax.stem(x,y,linefmt='r-',markerfmt=' ')
plt.setp(sl, linewidth=0.5)
plt.setp(bl, color="none")
ax.grid()
ax.set_xlim([0,2])
ax.set_ylim([0,1.2])
plt.xlabel('Größ $x$ (m)')
plt.subplots_adjust(left=0.17,\
  right=0.97, top=0.97, bottom=0.15)
plt.savefig('impulsplot.pdf')
plt.show()


# %%
# Step funktion 12 Schritte
fig2, ax2 = plt.subplots()
np.random.seed(0)
xmin = 0
xmax = 2.4
maxnum = 12
x2 = np.concatenate(([xmin], np.sort(np.random.normal(xavg, xsigma, maxnum)), [xmax]))
y2 = np.concatenate(([0], np.array(range(maxnum))/maxnum, [1]))
ax2.step(x2,y2)
ax2.set_xlim([xmin,xmax])
ax2.set_ylim([-0.1,1.2])
plt.xlabel('Größ $x$ (m)')
ax2.grid()
plt.subplots_adjust(left=0.17,\
  right=0.97, top=0.97, bottom=0.15)
plt.savefig('12schritte.pdf')
plt.show()

# %%
# Step funktion 12 Schritte
fig2, ax2 = plt.subplots()
np.random.seed(0)
xmin = 0
xmax = 2.4
maxnum = 12000
x2 = np.concatenate(([xmin], np.sort(np.random.normal(xavg, xsigma, maxnum)), [xmax]))
y2 = np.concatenate(([0], np.array(range(maxnum))/maxnum, [1]))
ax2.step(x2,y2)
ax2.set_xlim([xmin,xmax])
ax2.set_ylim([-0.1,1.2])
plt.xlabel('Größ $x$ (m)')
ax2.grid()
plt.subplots_adjust(left=0.17,\
  right=0.97, top=0.97, bottom=0.15)
plt.savefig('12000schritte.pdf')
plt.show()




# %%
# 12000 Schritte mit erf
fig2, ax2 = plt.subplots()
np.random.seed(0)
maxnum = 12000
x2 = np.concatenate(([xmin], np.sort(np.random.normal(xavg, xsigma, maxnum)), [xmax]))
y2 = np.concatenate(([0], np.array(range(maxnum))/maxnum, [1]))
ax2.step(x2,y2)
ax2.set_xlim([0,2.4])
ax2.set_ylim([-0.1,1.2])
import scipy.special
import math
xc = np.linspace(0, xmax, 70)
yc = scipy.special.erf((xc-xavg)/(xsigma*math.sqrt(2)))*0.5+0.5
ax2.plot(xc, yc, 'rx')
ax2.set_xlim([xmin,xmax])
ax2.set_ylim([-0.1,1.2])
plt.xlabel('Größ $x$ (m)')
ax2.grid()
plt.subplots_adjust(left=0.17,\
  right=0.97, top=0.97, bottom=0.15)
plt.savefig('12000schritteunderf.pdf')
plt.show()





# %%
