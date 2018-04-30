import math
from math import acos, sin, cos, pi, ceil, sqrt

c = 46.9
p = 0.050


def way(h, alp):
    alpha = acos(1/(1+h))

    if alp > 2 * alpha:
        ans = (2*(1+h)*(sin(alpha)*(alp//(2*alpha)) + cos((alp//(2*alpha))*alpha)))/c+p*ceil(alp/2/alpha)
    else:
        ans = 2*sqrt(1+(1+h)**2-2*(1+h)*cos(alp/2))/c+p
    return ans

def way_(h):
    d = 0
    for a in range(0, 31, 1):
        d = d + way(h, pi)
    return d / 31

import matplotlib as mpl
import matplotlib.pyplot as plt
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (1920 /2.5 / dpi, 1080 /2.5 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 1, 0, 1])

plt.title('t')
plt.xlabel('h')
plt.ylabel('t(h), s')

xs = []
vals = []

x = 0
minv = 100
minvx = -1
while x < 6:
    x += 10**(-3)
    way__ = way_(x)
    if (minv >= way__):
    	minvx = x
    	minv = way__
    vals += [way__]
    xs += [x]
print(minvx, minv)
plt.plot(xs, vals, color = 'blue', linestyle = 'solid',
         label = 't(h)')

plt.legend(loc = 'upper right')
fig.savefig('trigan.png')