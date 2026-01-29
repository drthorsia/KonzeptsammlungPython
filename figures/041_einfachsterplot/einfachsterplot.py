t=[k for k in range(0,round(70/0.2))]
tbl=[1/(1+k*0.2) for k in t]
import matplotlib
matplotlib.pyplot.plot(t,tbl)
matplotlib.pyplot.grid()
matplotlib.pyplot.savefig('einfachsterplot.pdf')