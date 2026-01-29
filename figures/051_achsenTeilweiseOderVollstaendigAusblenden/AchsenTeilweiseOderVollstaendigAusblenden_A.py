import matplotlib.pyplot as plt
import os
t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig1, ax1 = plt.subplots()
p1 = ax1.plot(t, y, color="blue", linewidth=2)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title("Achsen teilweise ausblenden", fontsize=10, fontweight="bold")

ax1.spines['bottom'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.grid(True)
fig1.set_size_inches(102.4/25.4 , 76.8/25.4)
fig1.tight_layout()
fig1.savefig("AchsenTeilweiseOderVollstaendigAusblenden_A.pdf")
