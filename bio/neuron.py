# Neural Network Model: 
# 	http://end.wikipedia.org/wiki/Artificial_neuron#Spreadsheet_example 

from pkg.graphics import * 
from pkg.utils import * 
from settings import * 

NEURON_COLORS = [ {"red":255,"green":0,"blue":0}, # SENSORIAL NEURON 
				  {"red":255,"green":255,"blue":0}, # TRANSMITTER NEURON 
				  {"red":0,"green":0,"blue":255}, # TERMINAL NEURON 
				  {"red":0,"green":255,"blue":0} ] # MOTOR NEURON 

class Neuron: 
	def __init__(self,neuron_type,weight,id_number = 0): 
		self.type = neuron_type 
		self.id = id_number 
		self.th = 0.5 	# threshold 
		self.lr = 0.2 	# learning rate 
		self.w = weight # weight value 
		self.axon = [] # connection to other neurons 
		self.sub = 0 	# subtotal value of sensor and weight 
		self.hits = 0 
		self.body = Circle(Point(0,0),NEURON_SIZE) 
		self.x = 0 
		self.y = 0 

	def is_type(self,neuron_type): 
		return self.type==neuron_type 

	# ======================== 
	# bio processes 
	# ======================== 
	def process(self,sensor): 
		if(sensor>0): 
			self.lightup() 
			
			# @TODO change 2 to TERMINAL 
			if(self.is_type(2)): 
				self.hits += 1 
			else: 
				expected = 1 if bool(sensor) else 0 # desired output 
				self.sub += sensor*self.w # accumulated value 
				error = expected 
				out = 0 

				# determine whether there's a value to send 
				while(self.sub>self.th): 
					out = 1 
					self.sub -= self.th 
					error = expected-out 
					self.learn(error) 
					self.send(out) 

				self.learn(error) 
				self.send(out) 
			
			self.lightdown() 

	def learn(self,error): 
		correction = self.lr if (error==1) else -self.lr/2 
		self.w += correction # corret weight value based on error 

	def send(self,out): 
		for synapse in self.axon: 
			synapse.process(out) 

	def add_synapse(self,neuron): 
		self.axon.append(neuron) 

	# ======================== 
	# graphic processes 
	# ======================== 
	def draw(self,win,x,y): 
		self.x = x 
		self.y = y 
		point = Point(x,y) 
		self.body = Circle(point,NEURON_SIZE) 
		self.body.draw(win) 

	def lightup(self): 
		c = NEURON_COLORS[self.type]
		r = c["red"] 
		g = c["green"] 
		b = c["blue"] 
		color = color_rgb(r,g,b) 
		self.body.setFill(color) 

	def lightdown(self): 
		color = color_rgb(255,255,255) 
		self.body.setFill(color) 

	def get_coords(self): 
		return self.x, self.y 
