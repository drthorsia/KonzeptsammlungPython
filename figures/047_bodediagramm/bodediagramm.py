import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal 

# Uebertragungsfunktion F(p) = 1/T1p+1 (Tiefpass 1.Ordnung)
num = [1]
den = [1, 1]
system = signal.TransferFunction(num, den)

# Frequenzbereich Logarithmisch waehlen
w = np.logspace(-2, 2, 500) # von 10^-2 bis 10^2 rad/s

# Frequenzgang berechnen 
w, mag, phase = signal.bode(system, w=w)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))

# Betrag in dB
ax1.semilogx(w, mag)
ax1.set_title("Bode-Diagramm", fontsize=10, fontweight="bold")
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(True, which="both", linestyle="--", linewidth=0.5)

# Phase in Grad
ax2.semilogx(w, phase)
ax2.set_xlabel('Kreisfrequenz (rad/s)')
ax2.set_ylabel('Phase (Grad)')
ax2.grid(True, which="both", linestyle="--", linewidth=0.5)

fig.set_size_inches(200/25.4, 150/25.4) # Umwandlung von millimeter in Zoll 
plt.tight_layout() # sorgt fuer schoene Abstaende
plt.savefig('bodediagramm.pdf')
