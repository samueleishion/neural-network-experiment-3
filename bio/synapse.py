from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from settings import * 

class Synapse: 
	def __init__(self,neuron_from,neuron_to): 
		self.neuron_from = neuron_from 
		self.neuron_to = neuron_to 
		self.line = None 

	def draw(self,win): 
		p1 = self.neuron_from.body.getCenter() 
		p2 = self.neuron_to.body.getCenter() 
		self.line = Line(p1,p2) 
		self.line.setFill(color_rgb(200,200,200)) 
		self.line.draw(win) 

	def erase(self): 
		print "erasing synapse between neurons "+str(self.neuron_from.id)+" and "+str(self.neuron_to.id)
		self.line.move(1000,1000)
		self.line = None 