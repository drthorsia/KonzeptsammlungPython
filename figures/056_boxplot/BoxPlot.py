import numpy as np
import matplotlib.pyplot as plt

# Zufallsdaten erstellen
np.random.seed(0)
N = 70
data_1 = np.random.normal(100, 10, N)
data_2 = np.random.normal(90, 20, N)
data_3 = np.random.normal(80, 30, N)
data = [data_1, data_2, data_3]

fig, ax = plt.subplots()
fig.set_size_inches(132.4/25.4, 96.8/25.4)

# Boxplot erstellen
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0)

# Farben anpassen
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Linien anpassen
for whisker in bp['whiskers']:
    whisker.set(color='#8B008B', linewidth=1.5, linestyle=":")

for cap in bp['caps']:
    cap.set(color='#8B008B', linewidth=2)

for median in bp['medians']:
    median.set(color='red', linewidth=3)

for flier in bp['fliers']:
    flier.set(marker='D', color='#e7298a', alpha=0.5)

print("data_1 : ", data_1)
print(f"\n data_2 :  {data_2}")
print(f"\n data_3 :  {data_3}")

# Statistische Werte berechnen und anzeigen
for i, d in enumerate(data, start=1):
    Q1 = np.percentile(d, 25)
    Q3 = np.percentile(d, 75)
    IQR = Q3 - Q1

    lower_whisker = Q1 - 1.5 * IQR
    upper_whisker = Q3 + 1.5 * IQR

    outliers = d[(d < lower_whisker) | (d > upper_whisker)]

    print(f"\n Datensatz {i}: data_{i}")
    print(f"Q1 (25%): {Q1:.2f}")
    print(f"Q3 (75%): {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Unterer Whisker (Grenze): {lower_whisker:.2f}")
    print(f"Oberer Whisker (Grenze): {upper_whisker:.2f}")
    print(f"Ausreißer: {outliers if len(outliers) > 0 else 'Keine'}")

plt.xlabel('$Datensatz$')
plt.ylabel('$Messwert$')
plt.title("BoxPlot Diagramm", fontsize=10, fontweight="bold")
plt.grid()
plt.savefig('Box-Plot.pdf')
plt.show()
