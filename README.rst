Maps with Measurement Uncertainty
====================================

This is an attempt at implementing uncertainty Visualisation with matplotlib.
I want to show measured value and uncertainty in the same image,
like here:

.. image: http://spatial-analyst.net/wiki/index.php/File:Fig_comparison_visualisation.jpg

Examples
=========

Lets say we have this observation:

.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_value.png

And the uncertainty increases from center to outside:

.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_error.png

Here are some attempts:

1) This whitens with increasing error:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_spring.png

2) Cool color map:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_cool.png

3) This one grays out:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_plasma.png

4) With viridis color map:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_viridis.png

5) Winter:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_winter.png

6) Some color maps do not work well, like Red-Blue. This is because the middle is too bright.

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_observation_RdBu.png


Approach
=============

There are two axes: value is mapped to hue/color, and error should modify either lightness or saturation.

Modern colormaps are perceptually uniform. They increase the lightness/luma in lockstep with the color.

Here however we two independent axes, like here:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_colorspace.png

On the vertical axis are different colors. Towards the right, the image desaturates (with increasing uncertainty).

The nice thing about this approach is that in a black-and-white print-out, only one axis is lost (saturation), but the vertical axis (lightness) still goes with value.

Here is the same image, grayscaled:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/demo_colorspace_gray.png


The first approach is to go to a colorspace such as JCh or HSV that have color (Hue H) and lightness or saturation as independent axes (V,J). This gives images like this one:

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/cam-JCh.png
		:alt: JCh

	.. image: https://raw.githubusercontent.com/JohannesBuchner/uncertaincolors/master/cam-CAM.png
		:alt: CAM02-UCS

The arcs make the image useless. Colors here are not desaturized homogeneously.

Instead, the approach I chose is to select a colormap and get the initial values (at uncertainty 0) and find their saturation. I normalise the colormaps to the same saturation. The second axis then desaturates until no color is left.

Code can be found in https://github.com/JohannesBuchner/uncertaincolors/blob/master/uncertaincolors.py





