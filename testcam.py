import numpy
import matplotlib.pyplot as plt
from colorspacious import cspace_convert

x = numpy.linspace(-1,1, 500)
y = numpy.linspace(-1,1, 500)
X, Y = numpy.meshgrid(x, y)
value = numpy.abs(X) #**0.5 * X/numpy.abs(X) #+ 0.25
error = (X**2 + Y**2)**0.5 * 0.5
value = (-Y+1)/2.
error = (X+1)/2.
"""
plt.imshow(value)
plt.colorbar()
plt.savefig('value.pdf', bbox_inches='tight')
plt.close()

plt.imshow(error)
plt.colorbar()
plt.savefig('error.pdf', bbox_inches='tight')
plt.close()
"""
total = numpy.zeros((value.shape[0], value.shape[1], 3))

h = value
l = error**0.5
l[l<0]=0
l[l>1]=1
"""
#Jp = 150 * l + 10
#radius = 40

#Jp = 150 * l + 10
Jmax = 100
Jp = Jmax * l + 10
radius = 20
b0 = 10
a0 = 20
for a0 in range(0, 80, 5):
	for b0 in range(0, 80, 5):

		ap = radius * numpy.sin(h * 2 * numpy.pi) + a0
		bp = radius * numpy.cos(h * 2 * numpy.pi) + b0

		colors = numpy.dstack((Jp, ap, bp))
		total = cspace_convert(colors, 'CAM02-UCS', 'sRGB1')
		total[total<0] = 0
		total[total>1] = 1
		plt.imshow(total)
		plt.savefig('cam_%d_%d_%d_%d.png' % (Jmax, radius,a0,b0), bbox_inches='tight')
		plt.close()
"""
Jmax = 100
Jp = Jmax * l + 20
radius = 40
b0 = 0
a0 = 0
circle_fraction = 0.25

ap = radius * numpy.sin(h * 2 * numpy.pi * circle_fraction) + a0
bp = radius * numpy.cos(h * 2 * numpy.pi * circle_fraction) + b0

colors = numpy.dstack((Jp, ap, bp))
total = cspace_convert(colors, 'CAM02-UCS', 'sRGB1')

total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('cam-CAM.png', bbox_inches='tight')
plt.close()

#  J (for lightness), C (for chroma), and h (for hue)
H = 100 * h
#J = l * 110 + 10
J = 50 + 0 * l
C = 250 * (1 - l)
colors = numpy.dstack((J, C, H))
total = cspace_convert(colors, "JCh", "sRGB1")


total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('cam-JCh.png', bbox_inches='tight')
plt.close()

"""
for i in range(len(x)):
	for j in range(len(y)):
		h = value[i,j] / 2 + 0.5
		h = numpy.fmod(h + 2, 1)
		
		l = error[i,j]**0.5
		l = max(min(l, 1), 0)
		#Jp = 75 * l
		Jp = 150 * l + 10
		radius = 40
		Jp = 100
		radius = 60 * (1 - l)
		ap = radius * numpy.sin(h * 2 * numpy.pi)
		bp = radius * numpy.cos(h * 2 * numpy.pi)
		
		rgb = cspace_convert([Jp, ap, bp], 'CAM02-UCS', 'sRGB1')
		rgb[rgb < 0] = 0
		rgb[rgb > 1] = 1
		#print(rgb)
		total[i,j,:] = rgb
"""

