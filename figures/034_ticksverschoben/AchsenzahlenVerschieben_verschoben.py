import matplotlib.pyplot as plt
import matplotlib.transforms

t = [k for k in range(10)]
y = [1/(k+1) for k in t]

fig, ax1 = plt.subplots() 

# Erstes Bild ohne Achsenzahlen Verschiebeung 
p1 = ax1.plot(t, y, color="blue", linewidth=2)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.xaxis.set_tick_params(pad=-15)
ax1.set_title("Achsenzahlen nicht verschoben", fontsize=10, fontweight="bold")
ax1.grid(True)


fig.set_size_inches(128/25.4 , 69/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende
Breite_inches=2.2
Hoehe_inches=0.7
xmin_inches=0.6
ymin_inches=0.3
plt.savefig('Achsenzahlenverschieben_verschoben.pdf', bbox_inches=matplotlib.transforms.Bbox([[xmin_inches, ymin_inches],[xmin_inches+Breite_inches,Hoehe_inches+ymin_inches]]))
#plt.show()

