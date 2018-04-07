import numpy
import colorsys
from matplotlib.colors import hsv_to_rgb


def to_rgb(value, error):
	z = value
	f1 = -90 - z*300
	f2 = f1 + 360 if f1 <= -360 else f1
	h = f2 * 240 / 360. if f2 >= 0 else (f2+360)*240/360.
	
	e = error
	e = max(min(e, 1), 0)
	s = 240 * (1 - e)
	v = 125 * (1 + e)
	rgb = colorsys.hsv_to_rgb(h/255.,s/255.,v/255.)
	return rgb

def all_to_rgb(value, error):
	z = value
	#f1 = -90 - z*300
	#f2 = numpy.where(f1 <= -360, f1 + 360, f1)
	#h = numpy.where(f2 >= 0, f2 * 240 / 360., (f2+360)*240/360.)
	#h = numpy.fmod((z+0.65)*255, 255) #*240/360
	h = z * 200 + 20
	
	e = error
	e = numpy.where(e >= 0, numpy.where(e <= 1, e, 1), 0)
	s = 240 * (1 - e)
	v = 125 * (1 + e)
	hsv = numpy.dstack((h, s, v)) / 255.
	print('hsv shape:', hsv.shape)
	return hsv_to_rgb(hsv)


if __name__ == '__main__':
	import matplotlib.pyplot as plt

	x = numpy.linspace(-1,1, 500)
	y = numpy.linspace(-1,1, 500)
	X, Y = numpy.meshgrid(x, y)
	value = (-Y+1)/2.
	error = (X+1)/2.
	total = all_to_rgb(value, error**0.5)
	plt.imshow(total)
	plt.xlabel('Uncertainty')
	plt.ylabel('Value')
	plt.savefig('demo_colorspace.pdf', bbox_inches='tight')
	plt.close()


	value = numpy.abs(X)
	error = (X**2 + Y**2)**0.5
	total = all_to_rgb(value, error**0.5)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation.pdf', bbox_inches='tight')
	plt.close()


