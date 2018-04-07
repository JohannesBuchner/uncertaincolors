import numpy
import colorsys
from matplotlib import pyplot as plt
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

def all_to_rgb(value, error, cm=plt.cm.cool, lo=0, hi=1):
	x = numpy.linspace(0, 1, 400)
	colors = cm(x*(hi - lo) + lo)[:,:3]
	#J, C, H = cspace_convert(colors, 'sRGB1', satspace).transpose()
	H, S, V = rgb_to_hsv(colors).transpose()
	frac = S.min() / S

	colors = cm(value.flatten()*(hi - lo) + lo)[:,:3]
	H, S, V = rgb_to_hsv(colors).transpose()
	S *= numpy.interp(x=value.flatten(), xp=x, fp=frac)
	error = numpy.where(error >= 0, numpy.where(error <= 1, error, 1), 0)
	S *= 1 - error.flatten()

	total = hsv_to_rgb(numpy.dstack((H, S, V)))
	total = total.reshape(value.shape[0], value.shape[1], 3)
	total[total<0] = 0
	total[total>1] = 1
	return total

if __name__ == '__main__':
	import matplotlib.pyplot as plt

	x = numpy.linspace(-1,1, 500)
	y = numpy.linspace(-1,1, 500)
	X, Y = numpy.meshgrid(x, y)
	
	value = (-Y+1)/2.
	error = (X+1)/2.
	total = all_to_rgb(value, error, cm=plt.cm.viridis_r, hi=0.5)
	plt.imshow(total)
	plt.xlabel('Uncertainty')
	plt.ylabel('Value')
	plt.savefig('demo_colorspace.png', bbox_inches='tight')
	plt.close()

	value = numpy.abs(X)
	error = (X**2 + Y**2)**0.5
	plt.title('Measurement Value')
	plt.imshow(value)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.colorbar()
	plt.savefig('demo_observation_value.png', bbox_inches='tight')
	plt.close()
	plt.imshow(error)
	plt.title('Measurement Error')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.colorbar()
	plt.savefig('demo_observation_error.png', bbox_inches='tight')
	plt.close()
	
	total = all_to_rgb(value, error, cm=plt.cm.viridis_r, hi=0.5)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_viridis.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.cool_r)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_cool.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.plasma_r, hi=0.6)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_plasma.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.winter)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_winter.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.spring)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_spring.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.summer)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_summer.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.RdBu_r)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_RdBu.png', bbox_inches='tight')
	plt.close()

	total = all_to_rgb(value, error, cm=plt.cm.coolwarm)
	plt.imshow(total)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig('demo_observation_coolwarm.png', bbox_inches='tight')
	plt.close()


