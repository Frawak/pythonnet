# Standard library imports
from abc import ABC, abstractmethod
import math
import random

# CLR imports
import clr
clr.AddReference("piweb_formplots/Zeiss.PiWeb.Formplot")
from Zeiss.PiWeb.Formplot.FileFormat import Segment, SegmentTypes, Tolerance
from Zeiss.PiWeb.Formplot.FileFormat import CylindricityPlot, CylinderPoint, CylinderGeometry
from Zeiss.PiWeb.Formplot.FileFormat import StraightnessPlot, LinePoint, LineGeometry


class Vec3d:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


class Formplot(ABC):
	@abstractmethod
	def get_plot(self):
		return None
		
	def check_add_segment(self, plot, current_segment, current_index,
					      point_type, geometry_type, segment_type,
						  segment_name: str = None):
		i = current_index
		if segment_name is None:
			segment_name = f"Segment {i}"
		if i == 0:
			current_segment = Segment[point_type, geometry_type](segment_name, segment_type)
			plot.get_Segments().Add(current_segment)
		return current_segment
	
	
class Straightness(Formplot):
	def __init__(self):
		self.count = 199
	
	def get_plot(self):
		plot = StraightnessPlot()
		
		plot.Actual.Length = 5.0
				
		plot.Tolerance = Tolerance(-0.1, 0.1)
		
		segment = None
		
		for i in range(self.count):
			segment = self.check_add_segment(plot, segment, i, LinePoint, LineGeometry, getattr(SegmentTypes, "None"))
				
			position = i / self.count
			deviation = 0.1 * (math.sin(position * 2.0 * math.pi) + (next_random()) * 0.2)
			
			point = LinePoint(position, deviation)
			segment.get_Points().Add(point)
			
		return plot
	

class Cylindricity(Formplot):
	def __init__(self):
		self.count = 23490
		self.coordinates = [Vec3d(next_random(), next_random(), next_random()) for i in range(self.count)]
	
	def get_plot(self):
		spins = 4
		
		plot = CylindricityPlot()
		
		plot.Actual.Height = 10
		
		plot.Tolerance = Tolerance(-0.1, 0.1)
		
		segment = None
		
		for i in range(self.count):
			segment = self.check_add_segment(plot, segment, i, CylinderPoint, CylinderGeometry, getattr(SegmentTypes, "None"))
			
			angle = i / self.count * 2.0 * spins * math.pi
			deviation = 0.1 * (math.sin(angle) + (next_random()) * 0.2)
			height = i / self.count
			
			point = CylinderPoint(angle, height, deviation)
			segment.get_Points().Add(point)
			
		return plot
	

#### Help functions ####

def next_random():
	return random.uniform(0.0, 1.0) - 0.5

