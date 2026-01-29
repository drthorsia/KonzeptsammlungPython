import matplotlib.pyplot as plt 
import numpy as np
xv = np.linspace(-2, 2, 10)
yv = np.linspace(4, 1, 5)
Mx, My = np.meshgrid(xv, yv)
Mz = np.sqrt(Mx**2+My**2)
fig, ax = plt.subplots()
fig.set_size_inches(200/25.4, 150/25.4)
ax.imshow(Mz, extent = [-5, 2, -3, 4], aspect = 'auto',
          cmap = 'jet', interpolation = 'none')
ax.grid(lw = 1)
ax.set_title('Pixelanzeige einer Matrix')
ax.title.set_fontsize(10)
ax.title.set_fontweight("bold")
plt.savefig('Pixelanzeige_einer_Matrix.pdf')
plt.show()
