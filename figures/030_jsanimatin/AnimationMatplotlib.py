#%%
# Quelle: http://louistiao.me/posts/notebooks/
#    embedding-matplotlib-animations-in-jupyter-as-
#    interactive-javascript-widgets/
%matplotlib inline
plt.rcParams['axes.facecolor']='white'
plt.rcParams['savefig.facecolor']='white'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

fig, ax = plt.subplots()
ax.set_xlim(( 0, 7))
ax.set_ylim((-2, 2))
line, = ax.plot([], [], lw=2)
draw_circle = plt.Circle((0.5, 0.5), 0.3)
ax.add_patch(draw_circle)
ax.set_aspect('equal')
ax.grid()

def init():
    line.set_data([], [])
    return (line,)

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    draw_circle.center=(i/20,0)
    line.set_data(x, y)
    return (line,)
# interval: Framedauer in ms
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, 
                               blit=True)
HTML(anim.to_jshtml())