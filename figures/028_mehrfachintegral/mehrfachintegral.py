#%%
import numpy as np
from scipy import integrate

def bunten(apar):
    return(np.sin(apar))

def boben(apar):
    return(apar**2)

def integrand(apar, bpar):
    return(apar*bpar)

res = integrate.dblquad(integrand, 2, 5, bunten, boben, epsabs=1.5e-8, epsrel=1.5e-8)[0]
print(res)
