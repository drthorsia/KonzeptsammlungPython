import numpy as np
import pandas as pd

xy = [\
      (20, 0),\
      (16, 3),\
      (15, 7),\
      (16, 4),\
      (13, 6),\
      (10, 10),\
      ]
df = pd.DataFrame(xy, columns=['x', 'y'])
print(df)
# Mittelwert = Summe durch Anzahl
x_avg = df['x'].sum()/df['x'].count() 
y_avg = df['y'].sum()/df['y'].count()
y_avg2 = df['y'].mean() #geht auch
# Erzeugung neuer Spalten:
df['Dx'] = df['x']-x_avg
df['Dy'] = df['y']-y_avg
df['Dx*Dy'] = df['Dx']*df['Dy']
df['Dx^2'] = df['Dx']**2
m = df['Dx*Dy'].sum()/df['Dx^2'].sum() # Steigung
b = y_avg-m*x_avg # Offset
print(df)

# Ergebnis plotten:
import matplotlib.pyplot as mpl
fix, ax = mpl.subplots()
ax.plot(df['x'],df['y'], 'rx')
ax.plot(df['x'],m*df['x']+b, 'b-')
mpl.grid()
mpl.xlabel('x')
mpl.ylabel('y')
mpl.savefig('LinRegPandas.pdf')
