import matplotlib.pyplot as plt
import os
t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
p2 = ax2.plot(t, y, color="blue", linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y$')
ax2.set_title("Achsen vollständig ausblenden", fontsize=10, fontweight="bold")

ax2.spines['top'].set_color('none')
ax2.spines['right'].set_color('none')
ax2.spines['bottom'].set_color('none')
ax2.spines['left'].set_color('none')
ax2.grid(True)
fig2.set_size_inches(102.4/25.4 , 76.8/25.4) 
fig2.tight_layout()  
fig2.savefig("AchsenTeilweiseOderVollstaendigAusblenden_B.pdf")
