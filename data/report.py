from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from bio.neuron import * 
from bio.organ import * 
from bio.network import * 
from bio.synapse import * 
from settings import * 

class Report: 
	def __init__(self,network): 
		self.network = network 
		self.graphs = [] 

		for organ in self.network.organs: 
			graph = Graph(organ.id)
			self.graphs.append(graph) 


	def draw(self,win): 
		r = Rectangle(Point(0,WINDOW_Y-210),Point(WINDOW_X,WINDOW_Y)) 
		c = color_rgb(220,220,220) 
		r.setFill(c) 
		r.setOutline(c)
		r.draw(win) 

		space = WINDOW_X*1.0
		x_offset = 30 
		for graph in self.graphs: 
			graph.draw(win,x_offset,WINDOW_Y-200,190/SENSORY_NEURONS) 
			x_offset += space/3


class Graph: 
	def __init__(self,organ_id): 
		self.id = organ_id 
		self.matrix = [[None]*TERMINAL_NEURONS]*SENSORY_NEURONS 

	def draw(self,win,left,top,size): 
		y = top  
		for row in self.matrix: 
			x = left 
			for col in row: 
				r = Rectangle(Point(x,y),Point(x+size,y+size)) 
				r.setFill(color_rgb(255,255,255))
				r.draw(win) 
				x += size 
			y += size 