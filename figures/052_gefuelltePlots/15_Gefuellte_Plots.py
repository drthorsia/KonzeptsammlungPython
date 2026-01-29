import matplotlib.pyplot as plt 
import numpy as np
fig, ax = plt.subplots()
xorig = np.linspace(0, 1 ,30)
x = np.append([0], xorig)
y = np.append([0], np.sqrt(1-xorig**2))
ax.fill(x, y)
ax.plot(x, y, 'k-')
plt.grid()
plt.title("Gefüllte Plots", fontsize=10, fontweight="bold")
fig.set_size_inches(102.4/25.4 , 76.8/25.4) 
plt.savefig('GefuelltePlots.pdf')
plt.show()
