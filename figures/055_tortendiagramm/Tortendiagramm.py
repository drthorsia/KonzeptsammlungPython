import matplotlib.pyplot as plt

labels = 'Stromkosten', 'Nebenkosten', 'Kaltmiete', 'Internet'
sizes = [51, 72.90, 462.95, 49.99]
# Das zweites Stueckt ist nicht/leicht herausgezogen
explode = (0, 0.1, 0, 0)
explode = (0, 0.0, 0, 0) # nicht herausgezogen
fig, ax = plt.subplots()
fig.set_size_inches(102.4/25.4 , 76.8/25.4)
ax.set_title("Tortendiagramm für Kosten einer Mietwohung")
ax.title.set_fontsize(10)
ax.title.set_fontweight("bold")
ax.pie(sizes, explode=explode, labels=labels,
       autopct= lambda p: f'{p*sum(sizes) / 100:.1f} €',
        shadow=False, startangle=0)
ax.axis('equal') # Der Kuchen wird als Kreis gezeichnet
plt.savefig('Tortendiagramm.pdf')
plt.savefig('Tortendiagramm.svg')
