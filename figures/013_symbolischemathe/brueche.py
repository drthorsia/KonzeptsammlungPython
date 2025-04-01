# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:55:07 2020

@author: thor
"""
#import math 
from math import pi
from sympy import *
import sympy
by =  sympy.symbols('by') #Rational(1,19)
bx = -1*(Rational(-8,19)*by-Rational(36,19))/2+\
    sympy.sqrt(((Rational(-8,19)*by-Rational(36,19))/2))**2-\
        (Rational(13,19)*by**2 - Rational(72,19)*by-Rational(27,19))
print(simplify(bx))
by = 19
bx = -1*(Rational(-8,19)*by-Rational(36,19))/2+\
    sympy.sqrt(((Rational(-8,19)*by-Rational(36,19))/2))**2-\
        (Rational(13,19)*by**2 - Rational(72,19)*by-Rational(27,19))
print(simplify(bx))
print(simplify(bx)*1.0)

from sympy.solvers import solve
#erg = solve(-Rational(13, 19)*by**2 + Rational(72,19)*by + Rational(27,19)-,by)
#print(erg)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, 1], [0, 0], [0, 0], '-g')
ax.plot([0, 0], [0, 1], [0, 0], '-b')
ax.plot([0, 0], [0, 0], [0, 1], '-r')
#plt.show()

import numpy as np
from numpy import linalg as LA
import math 
from math import cos
from math import sin
veca = np.array([[1],[2], [3]])*1/3 #Vektor a
vecanorm = veca/LA.norm(veca) # Normvektor von a
n = vecanorm
alpha = math.pi/6 # Drehwinkel
ax.plot([0,veca[0]],[0,veca[1]],[0,veca[2]])

ra =2.1
ax.set_xlim3d([-ra, +ra])
ax.set_ylim3d([-ra, +ra])
ax.set_zlim3d([-ra, +ra])

# zweiter Vektor z=3
by = Rational(19,4) 
bx = Rational(37,19)-sympy.sqrt(28497)/76

    #print()

bx, by = sympy.symbols('bx,by')
bbx = solve(sympy.sqrt(3)/2-(bx+2*by+9)/(sympy.sqrt(14)*sympy.sqrt(bx**2 + by**2 + 9)), bx)
print(bbx)

by = Rational(19,4)
bx = 4*by/19 - sympy.sqrt(-231*by**2 + 1512*by - 189)/19 + Rational(18,19)
bx = Rational(37,19)-sympy.sqrt(28497)/76
print(bx)
vecb = np.array([[float(bx)], [by*1.0], [3]])/(math.sqrt(bx**2+by**2+3**2))
ax.plot([0,vecb[0]],[0, vecb[1]],[0,vecb[2]])

vecc = vecb
alpha = math.pi/4
DrehMat = [[n[0]**2*(1-cos(alpha))+cos(alpha), n[0]*n[1]*(1-cos(alpha))-n[2]*sin(alpha), n[0]*n[2]*(1-cos(alpha))+n[1]*sin(alpha)],\
           [n[1]*n[0]*(1-cos(alpha))+n[2]*sin(alpha), n[1]**2*(1-cos(alpha))+cos(alpha), n[1]*n[2]*(1-cos(alpha))-n[0]*sin(alpha)],\
           [n[2]*n[0]*(1-cos(alpha))-n[1]*sin(alpha), n[2]*n[1]*(1-cos(alpha))+n[0]*sin(alpha), n[2]**2*(1-cos(alpha))+cos(alpha)]]

vecc = numpy.matmul(Drehmat,vecb)



winkelab = math.acos((veca[0]*vecb[0] + veca[1]*vecb[1] + veca[2]*vecb[2])/(math.sqrt(veca[0]**2+veca[1]**2+veca[2]**2)*math.sqrt(vecb[0]**2+vecb[1]**2+vecb[2]**2)))
winkelac = math.acos((veca[0]*vecb[0] + veca[1]*vecb[1] + veca[2]*vecb[2])/(math.sqrt(veca[0]**2+veca[1]**2+veca[2]**2)*math.sqrt(vecb[0]**2+vecb[1]**2+vecb[2]**2)))
print(winkel*180/math.pi)

