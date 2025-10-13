# 22.31 Sankey Diagramm

import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
import os

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Sankey Diagramm einer Halogenlampe") # xticks=[], yticks=[] Achsenmarkierungen werden entfernt
ax.title.set_fontsize(10)
ax.title.set_fontweight("bold")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='J')
sankey.add(flows=[35, -30, -5],
           labels=['Gesamte zugefuehrte Energie', 'Waermeenergie', 'Nutzenergie'],
           orientations=[0, -1, 0], # 0(inputs from the left, outputs to the right), 1(from and to the top) or -1(from and to the bottom)
           pathlengths=[0.25, 0.25, 0.25],
           patchlabel="Halogenlampe")  # Arguments to matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
fig.set_size_inches(200/25.4 , 150/25.4) # Umwandlung von millimeter in Zoll 
plt.savefig(os.path.join("C:/Users/E1AJRWG/KonzeptsammlungPython_Copy/Kapitel22_Matplotlib/Kapitel22_Grafiken", 
                          "Sankey Diagramm.png"), dpi=300, bbox_inches='tight')
plt.show()
