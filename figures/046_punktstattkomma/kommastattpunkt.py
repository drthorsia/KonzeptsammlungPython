import matplotlib.pyplot as plt
import matplotlib.ticker as tkr 

def func(x, pos): # formatter
  s1 = '{:1.1f}'.format(x)
  s2 = s1.replace('.',',')
  return s2
y_frmt = tkr.FuncFormatter(func)

t = [k for k in range(10)]
y = [1/(k+1) for k in t]
fig, ax = plt.subplots()
p1 = ax.plot(t, y)
ax.yaxis.set_major_formatter(y_frmt)
plt.savefig('kommastattpunkt.pdf')
