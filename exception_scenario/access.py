import pythonnet
pythonnet.load("coreclr")

from piweb_formplots_reduced import Cylindricity, Straightness

l = []

for i in range(3):
	l += [Straightness().get_plot()]
	l += [Cylindricity().get_plot()]
