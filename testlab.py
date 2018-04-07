import numpy
import math
import matplotlib.pyplot as plt
import colorsys
from colormath.color_objects import LuvColor, sRGBColor
from colormath.color_conversions import convert_color

x = numpy.linspace(-1,1, 50)
y = numpy.linspace(-1,1, 50)
X, Y = numpy.meshgrid(x, y)
value = numpy.abs(X) #**0.5 * X/numpy.abs(X) #+ 0.25
error = (X**2 + Y**2)**0.5 * 0.5

plt.imshow(value)
plt.colorbar()
plt.savefig('value.pdf', bbox_inches='tight')
plt.close()

plt.imshow(error)
plt.colorbar()
plt.savefig('error.pdf', bbox_inches='tight')
plt.close()

total = numpy.zeros((value.shape[0], value.shape[1], 3))

for i in range(len(x)):
	for j in range(len(y)):
		h = value[i,j] / 2 + 0.5
		h = math.fmod(h + 2, 1)
		#h = 0.25
		#v = 1 - h
		v = 0.
		l = error[i,j]**0.5
		l = max(min(l, 1), 0)
		rgb = convert_color(LuvColor(luv_l=l*100, luv_u=h*100, luv_v=v*100), sRGBColor)
		#print(rgb.get_value_tuple())
		rgb = [rgb.clamped_rgb_r, rgb.clamped_rgb_g, rgb.clamped_rgb_b]
		total[i,j,:] = rgb

plt.imshow(total)
plt.savefig('lab.pdf', bbox_inches='tight')
plt.close()

