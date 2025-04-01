# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:26:51 2021

@author: thor
"""


import numpy as np
import matplotlib.pyplot as plt
# Achtung: linspace in y Richtung abfallend
Mx, My = np.meshgrid(np.linspace(-2,2,10), np.linspace(4,1,5))
Mz = np.sqrt(Mx**2+My**2)
fig, ax= plt.subplots()
fig.set_size_inches(50/25.4, 50/25.4)
ax.imshow(Mz, extent=[-5, 2, -3, 4],\
   aspect='auto', cmap='jet', interpolation = 'none')
ax.grid(lw=1)

fig.show()
plt.savefig('imshow.pdf')
plt.savefig('imshow.png', dpi=300)
plt.close(fig)

'''
My = np.array([[x] for x in np.linspace(L, -L, Nh)])@np.ones((1,Nh))
Mx = np.ones((Nh,1)) @ np.array([[x] for x in np.linspace(-L, L, Nh)]).transpose()
print(My+Mx)

absv = np.sqrt(Mx**2+My**2)
phiv = np.arctan2(Mx,My)
resplane = (np.abs(np.angle((Mx+1j*My)*1j))<=math.pi/4)*1.0

fig, ax= plt.subplots()
fig.set_size_inches(50/25.4, 50/25.4)
ax.imshow(resplane, extent=[-L, L, -L, L], aspect='auto', cmap='jet', interpolation = 'none')
ax.grid(lw=0.3)

x = np.array([-3,0,3])
y = np.array([-3,0,-3])
ax.fill(x,y, fill=False, hatch='\\\\\\') 

fig.show()
plt.savefig('imshow.pdf')
plt.savefig('imshow.png', dpi=300)
plt.close(fig)


'''