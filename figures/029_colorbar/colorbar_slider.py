#%%
from __future__ import print_function
from ipywidgets import interact,\
interactive, fixed, interact_manual 
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as mpl
from matplotlib import cm
%matplotlib inline

def tsfig(t):
    x = np.linspace(-7,7,150)
    y = np.linspace(-5,5,150)
    X, Y = np.meshgrid(x,y)
    fig, ax = mpl.subplots()
    Z = np.cos(t)*Y+np.sin(t)*X - np.sqrt(X**2+Y**2)*np.cos(t-np.arctan(X/Y))
    ctr = ax.contourf( X, Y, np.abs(Z), 150, cmap=cm.jet)
    ax.set_aspect('equal')
    ax.grid()
    fig.colorbar(ctr)
    #fig.show() nutzlos, erzeugt eine Warnung "Matplotlib is currently using.."

interact(tsfig, t=(-4,4,0.1))