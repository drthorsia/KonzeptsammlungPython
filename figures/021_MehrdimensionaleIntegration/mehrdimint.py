from scipy import integrate
from math import pi, cos
import numpy as np
def integrant(r, phi, z):
    return(r**3)*7
E,F=integrate.tplquad(integrant,0,9,\
  lambda z:-pi/6, lambda z: pi/6,\
  lambda z, phi: cos(phi),\
  lambda z, phi: 7)
print(E) # Ergebnis
print(F) # Fehler