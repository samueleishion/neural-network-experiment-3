from pkg.utils import * 
from bio.neuron import * 
from settings import * 

class Organ: 
	def __init__(self,neuron_number): 
		self.neurons = []
		for i in range(neuron_number):
			n = Neuron(0,0.5,1)
			self.neurons.append(n) 

	def draw(self,win,x,y): 
		gap = NEURON_SIZE+2 
		offset_x = 0 
		offset_y = 0 
		for neuron in self.neurons:
			change_x = gap*offset_x 
			change_y = gap if offset_y==1 else -gap
			neuron.draw(win,x+change_x,y+change_y) 
			offset_x += 1
			offset_y = flip(offset_y) 


# ======================== 
# individual organs 
# ======================== 
class Hand(Organ): 
	def feel(self): 
		return 0 

class Eye(Organ): 
	def __init__(self,neuron_number): 
		self.cones = [] 
		self.neurons = self.cones 
		for i in range(neuron_number): 
			c = Cone() 
			self.cones.append(c) 

	def add_synapse(self,neuron): 
		for cone in self.cones: 
			cone.add_synapse(neuron) 

# color detectors for eye nerves/neurons 
class Cone: 
	def __init__(self): 
		self.r = Neuron(SENSORIAL,0.5,1) 
		self.g = Neuron(SENSORIAL,0.5,1) 
		self.b = Neuron(SENSORIAL,0.5,1) 
		self.axon = self.r.axon 

	def perceive(self,r,g,b): 
		self.r.process((r/255)*INTENSITY) 
		self.g.process((g/255)*INTENSITY) 
		self.b.process((b/255)*INTENSITY) 

	def draw(self,win,x,y): 
		point = Point(x,y) 
		self.body = Circle(point,NEURON_SIZE) 
		self.body.draw(win) 

	def add_synapse(self,neuron): 
		self.r.add_synapse(neuron) 
		self.g.add_synapse(neuron) 
		self.b.add_synapse(neuron) 

