import numpy
import math
import matplotlib.pyplot as plt
from uncertaincolors import to_rgb, all_to_rgb

x = numpy.linspace(-1,1, 50)
y = numpy.linspace(-1,1, 50)
X, Y = numpy.meshgrid(x, y)
value = numpy.abs(X) #**0.5 * X/numpy.abs(X) #+ 0.25
error = (X**2 + Y**2)**0.5
#value = (-Y+1)/2.
#error = (X+1)/2.

"""
plt.imshow(value)
plt.colorbar()
plt.savefig('value.pdf', bbox_inches='tight')
plt.close()

plt.imshow(error)
plt.colorbar()
plt.savefig('error.pdf', bbox_inches='tight')
plt.close()

relerror = error / numpy.abs(value)
relerror[relerror > 2] = 2
plt.imshow(relerror)
plt.colorbar()
plt.savefig('relerror.pdf', bbox_inches='tight')
plt.close()"""

total = numpy.zeros((value.shape[0], value.shape[1], 3))

for i in range(len(x)):
	for j in range(len(y)):
		"""
		h = value[i,j] + 0.5
		h = math.fmod(h+2.0, 1)
		r,g,b = colorsys.hls_to_rgb(h,0.5,1)
		# whiten
		luma = (3*r+6*g+b) / 10.
		# target luma
		l = error[i,j]**0.5 + 0.4
		l = max(min(l, 1), 0)
		luma_target = l
		#luma_target * 10 = 3 * r + 6 * g + b
		luma_diff = (luma_target - luma) * 10
		r = r * luma/luma_target
		g = g * luma/luma_target
		b = b * luma/luma_target
		total[i,j,:] = [r,g,b]
		"""
		"""
		h = value[i,j] + 2.5
		h = math.fmod(h, 1)
		#h = max(min(h, 1), 0)
		#l = relerror[i,j]**0.5
		l = error[i,j]**0.5 + 0.4
		l = max(min(l, 1), 0)
		s = 1
		rgb = colorsys.hls_to_rgb(h,l,s)
		total[i,j,:] = list(rgb)
		"""
		"""
		z = value[i,j]
		#z = math.fmod(z+2., 1)
		f1 = -90 - z*300
		f2 = f1 + 360 if f1 <= -360 else f1
		h = f2 * 240 / 360. if f2 >= 0 else (f2+360)*240/360.
		
		e = error[i,j]**0.5
		e = max(min(e, 1), 0)
		s = 240 * (1 - e)
		v = 125 * (1 + e)
		rgb = colorsys.hsv_to_rgb(h/255.,s/255.,v/255.)
		"""
		total[i,j,:] = to_rgb(value[i,j], error[i,j]**0.5)

total = all_to_rgb(value, error**0.5)
plt.imshow(total)
plt.savefig('hue-lightness.pdf', bbox_inches='tight')
plt.close()
"""
cm = plt.cm.viridis
total = numpy.zeros((value.shape[0], value.shape[1], 3))
for i in range(len(x)):
	for j in range(len(y)):
		h = value[i,j] + 2.
		h = math.fmod(h, 1)
		r,g,b,_ = cm(h)
		h,l,s = colorsys.rgb_to_hls(r,g,b)
		# now de-saturize
		s2 = 1 - (error[i,j]/error.max())
		s = max(min(s*s2, 1), 0)
		rgb = colorsys.hls_to_rgb(h,l,s)
		total[i,j,:] = list(rgb)

plt.imshow(total)
plt.savefig('viridis-saturation.pdf', bbox_inches='tight')
plt.close()


total = numpy.zeros((value.shape[0], value.shape[1], 3))
for i in range(len(x)):
	for j in range(len(y)):
		
		h = value[i,j] + 2
		h = math.fmod(h, 1)
		r,g,b,_ = cm(h)
		h,l,s = colorsys.rgb_to_hls(r,g,b)
		# now lighten
		l2 = 1 - (error[i,j]/error.max())
		l = error[i,j]**0.5 + 0.4
		l = max(min(l, 1), 0)
		l = max(min(l*l2, 1), 0)
		rgb = colorsys.hls_to_rgb(h,l,s)
		total[i,j,:] = list(rgb)

plt.imshow(total)
plt.savefig('viridis-lightness.pdf', bbox_inches='tight')
plt.close()
"""
