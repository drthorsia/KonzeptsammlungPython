# 22.28 Ortskurve

import numpy as np
import matplotlib.pyplot as plt
import os


# Uebertragungsfunktion F(jw) = 1 / (1 + jwT) Tiefpass 1er Ordnung mit T = 1
def F(w):
    return 1 / (1 + 1j*w)

# Frequenzbereich w waehlen
w = np.linspace(0, 20, 500)
F_vals = F(w) # F_vals enthaelt alle komplexen Punkte der Ortskurve


# Figure
plt.figure(figsize=(8,6))
plt.plot(F_vals.real, F_vals.imag, 'b-', label="Ortskurve") # F_vals.real, H_vals.imag Real- und Imaginaerteil


# fuer w = 0; w = w0 und w = undendlich markieren. Mit w0 = 1
points = {
    r"$\omega=0$": F(0),
    r"$\omega=1$": F(1),
    r"$\omega\to\infty$": 0
}

for label, val in points.items():
    x, y = (val.real, val.imag) if val != 0 else (0, 0)
    plt.plot(x, y, 'ro')
    plt.text(x+0.05, y+0.05, label, color='red')

# Zeiger hinzufuegen, um die Richtung von w zu zeigen 
mid = len(F_vals)//2
plt.arrow(F_vals.real[mid], F_vals.imag[mid],
          F_vals.real[mid+1]-F_vals.real[mid],
          F_vals.imag[mid+1]-F_vals.imag[mid],
          shape='full', head_width=0.02, color='green')

# Formatierung 
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlabel('$Real$')
plt.ylabel('$Imaginaer$')
plt.title("Ortskurve", fontsize=10, fontweight="bold")
plt.grid()
plt.axis("equal")
plt.legend()
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Ortskurve.png"), dpi=300, bbox_inches='tight')
plt.show()
