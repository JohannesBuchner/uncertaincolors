import numpy
import matplotlib.pyplot as plt
from colorspacious import cspace_convert

x = numpy.linspace(-1,1, 500)
y = numpy.linspace(-1,1, 500)
X, Y = numpy.meshgrid(x, y)
#value = numpy.abs(X) #**0.5 * X/numpy.abs(X) #+ 0.25
#error = (X**2 + Y**2)**0.5 * 0.5
value = (-Y+1)/2.
#value = 0 * value + 0.5
error = (X+1)/2.
#error = error**0.5

satspace = 'JCh'

#cm = plt.cm.cool
cm = plt.cm.viridis
x = numpy.linspace(0, 1, 400)
colors = cm(x)[:,:3]
J, C, H = cspace_convert(colors, 'sRGB1', satspace).transpose()
Jfrac = J.min() / J
Cfrac = C.min() / C
Hfrac = H.min() / H
#Jfrac = Jfrac * 0 + 1
#Cfrac = Cfrac * 0 + 1
#Hfrac = Hfrac * 0 + 1

colors = cm(value.flatten())[:,:3]
J, C, H = cspace_convert(colors, 'sRGB1', satspace).transpose()
J *= numpy.interp(x=value.flatten(), xp=x, fp=Jfrac)
J *= 1 - error.flatten()

total = cspace_convert(numpy.dstack((J, C, H)), satspace, 'sRGB1')
total = total.reshape(value.shape[0], value.shape[1], 3)
total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('cmapJ.pdf', bbox_inches='tight')
plt.savefig('cmapJ.png', bbox_inches='tight')
plt.close()

J, C, H = cspace_convert(colors, 'sRGB1', satspace).transpose()
C *= numpy.interp(x=value.flatten(), xp=x, fp=Cfrac)
C *= 1 - error.flatten()

total = cspace_convert(numpy.dstack((J, C, H)), satspace, 'sRGB1')
total = total.reshape(value.shape[0], value.shape[1], 3)

total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('cmapC.pdf', bbox_inches='tight')
plt.savefig('cmapC.png', bbox_inches='tight')
plt.close()

J, C, H = cspace_convert(colors, 'sRGB1', satspace).transpose()
H *= numpy.interp(x=value.flatten(), xp=x, fp=Hfrac)
H *= 1 - error.flatten()

total = cspace_convert(numpy.dstack((J, C, H)), satspace, 'sRGB1')
total = total.reshape(value.shape[0], value.shape[1], 3)
total[total<0] = 0
total[total>1] = 1
plt.imshow(total)
plt.savefig('cmapH.pdf', bbox_inches='tight')
plt.savefig('cmapH.png', bbox_inches='tight')
plt.close()

