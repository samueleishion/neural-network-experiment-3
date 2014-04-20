from pkg.utils import * 
from bio.neuron import * 
from settings import * 
import random 

class Organ: 
	def __init__(self,neuron_number,organ_id): 
		self.id = organ_id 
		self.neurons = []
		for i in range(neuron_number):
			rand = random.uniform(0.25,0.75) 
			n = Neuron(SENSORIAL,rand,1) 
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
	def __init__(self,neuron_number,organ_id): 
		self.id = organ_id 
		self.neurons = []
		for i in range(neuron_number): 
			rand = random.uniform(0.25,0.75) 
			r = Cone(SENSORIAL,rand,RED,i) # red 
			g = Cone(SENSORIAL,rand,GRN,i) # green 
			b = Cone(SENSORIAL,rand,BLU,i) # blue 
			self.neurons.append(r) 
			self.neurons.append(g) 
			self.neurons.append(b) 

	def add_synapse(self,neuron): 
		for cone in self.neurons: 
			return cone.add_synapse(neuron) 
