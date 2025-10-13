# 22.6 Kommas Statt Punkte 

import matplotlib.pyplot as plt 
import matplotlib.ticker as tkr 
import os 

def func(x, pos): # formatter
    s1 = '{:1.1f}'.format(x)
    s2 = s1.replace('.',',')
    return s2
y_frmt = tkr.FuncFormatter(func)

t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(y_frmt)
p1 = ax.plot(t, y, color="blue", linewidth=2)

fig.set_size_inches(200/25.4 , 150/25.4)
plt.title("Kommas statt Punkte", fontsize=10, fontweight="bold")
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.grid()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Kommas statt Punkte.png"), dpi=300, bbox_inches='tight')
plt.show()

