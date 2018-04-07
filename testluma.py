import numpy
import math
import matplotlib.pyplot as plt
from uncertaincolors import to_rgb, all_to_rgb

x = numpy.linspace(-1,1, 50)
y = numpy.linspace(-1,1, 50)
X, Y = numpy.meshgrid(x, y)
value = numpy.abs(X) #**0.5 * X/numpy.abs(X) #+ 0.25
error = (X**2 + Y**2)**0.5
value = (1-Y)/2.
error = (X+1)/2.

# define b and r

b = value # * 0.114 * 3
r = 1 + 0 * value * 0.299 * 3

# we know what grayscale values we want

luma = error**0.5

# we also know how luma is defined:

# luma = (r**2 * 0.299 + g**2 * 0.587 + b**2 * 0.114)**0.5

# this defines one color given the other two.

# solve for green:
#g = ((luma**2 - b**2 * 0.114 - r**2 * 0.299) / 0.587)**0.5
g = (luma - b*0.114 - r*0.299) / 0.587

total = numpy.dstack((r, g, b))
total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('luma.pdf', bbox_inches='tight')
plt.savefig('luma.png', bbox_inches='tight')
plt.close()



