import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-15, 15, 150)
fig, ax = plt.subplots()
fig.set_size_inches(120/25.4,80/25.4)
g1, = ax.plot(x,np.sin(x))
plt.savefig('bilddatei.png', dpi=300)