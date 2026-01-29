from pychartdir import *
data = [463, 72.9, 51 , 50]
labels = ["Miete", "Nebenkosten", "Strom", "Internet"]
c= PieChart(500, 300)
c.setPieSize(250, 140, 100)
c.addTitle("title")
c.set3D()
c.setData(data, labels)
c.setExplode()
c.makeChart("threedpie.png")
