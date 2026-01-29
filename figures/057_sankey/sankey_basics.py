import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Zwei Systeme")
sankey = Sankey(ax=ax, unit=None)
flows = [0.25, 0.15, 0.60, -0.10, -0.09, -0.25, -0.15, -0.10, -0.35]
# flows: Positiv: hinaus, Negativ, hinein
sankey.add(flows=flows, label='Eins',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
# orientation: -1: nach oben, 0:rechts, 1: nach unten
sankey.add(flows=[-0.25, 0.15, 0.1], label='Zwei',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
plt.axis('off') # Rahmen entfernen
fig.set_size_inches(120/25.4,80/25.4)
plt.subplots_adjust(left=0.0,\
  right=0.97, top=0.85, bottom=0.0)
fig.savefig('sankeydiag.pdf')
