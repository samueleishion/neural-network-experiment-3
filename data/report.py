from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from bio.neuron import * 
from bio.organ import * 
from bio.network import * 
from settings import * 

class Report: 
	def __init__(self,network): 
		self.network = network 

	def draw(self,win): 
		r = Rectangle(Point(0,WINDOW_Y-210),Point(WINDOW_X,WINDOW_Y)) 
		c = color_rgb(220,220,220)
		r.setFill(c) 
		r.setOutline(c)
		r.draw(win) 