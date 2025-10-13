# 22.30 Tortendiagramm

import matplotlib.pyplot as plt
import os

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Stromkosten', 'Nebenkosten', 'Kaltmiete', 'Internet'
sizes = [51, 72.90, 462.95, 49.99]
explode = (0, 0.1, 0, 0) # Das zweites Stueckt ist leicht herausgezogen

fig, ax = plt.subplots()
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 

ax.set_title("Tortendiagramm für Kosten einer Mietwohung")
ax.title.set_fontsize(10)
ax.title.set_fontweight("bold")
ax.pie(sizes, explode=explode, labels=labels, autopct= lambda p: f'{p*sum(sizes) / 100:.1f} €',
        shadow=True, startangle=90)
ax.axis('equal') # Der Kuchen wird als Kreis gezeichnet
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Tortendiagramm.png"), dpi=300, bbox_inches='tight')
plt.show()