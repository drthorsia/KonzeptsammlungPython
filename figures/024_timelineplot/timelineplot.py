# %%
# Quelle u.a.:https://matplotlib.org/3.1.3/gallery/lines_bars_and_markers/timeline.html
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
xavg = 1.5
xsigma = 0.15
fig, ax = plt.subplots()
fig.set_size_inches(220/25.4,90/25.4)
fristen = [('Antragsfrist Internationalisierungsmaßnamen Präsidium','2021-11-06'),\
          ('Start ISU', '2022-05-09'),\
          ('Ende ISU', '2022-05-20')\
          ]
dates = [datetime.strptime(d[1], "%Y-%m-%d") for d in fristen]
datumstring = [d[1] for d in fristen]
print(dates)
levels = np.tile([1, 2, 3, 4, 5, 6], int(np.ceil(len(dates)/6)))[:len(dates)]
x = [d for d in dates]
y = levels
ml, sl, bl = ax.stem(x,y,linefmt='r-',markerfmt='o')
plt.setp(sl, linewidth=0.5)
plt.setp(bl, color="none")
names = [d[0] for d in fristen]
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3), textcoords="offset points", va='top', ha="right")
for d, l, r in zip(dates, levels, datumstring):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3), textcoords="offset points", va='bottom', ha="right")
#ax.grid()
ax.set_xlim([datetime.strptime("2020-01-01", "%Y-%m-%d"), datetime.strptime("2022-06-01", "%Y-%m-%d")])
#ax.set_ylim([0,1.2])
# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=2))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
#plt.xlabel('Datum')
plt.subplots_adjust(left=0.17, right=0.97, top=0.97, bottom=0.15)
# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)
plt.savefig('Terminplan.pdf')
plt.show()


# %%
import math

#*****
y = [(1j)**(3*k-1)*(1-(-1)**k) for k in range(8)]
print(np.round(y))

#**
y = [(1j)**(k+1)*(1-(-1)**k) for k in range(8)]
print(np.round(y))

# %%
y = [(1j)**(3*k-1) for k in range(8)]
print(np.round(y))

#**
y = [(1j)**(k+1) for k in range(8)]
print(np.round(y))

# %%
