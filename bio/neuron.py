# Neural Network Model: 
# 	http://en.wikipedia.org/wiki/Artificial_neuron#Spreadsheet_example 

from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from bio.synapse import * 
from settings import * 
from time import sleep 
import random

NEURON_COLORS = [ {"red":255,"green":0,"blue":0}, # SENSORIAL NEURON 
				  {"red":255,"green":255,"blue":0}, # TRANSMITTER NEURON 
				  {"red":0,"green":0,"blue":255}, # TERMINAL NEURON 
				  {"red":0,"green":255,"blue":0} ] # MOTOR NEURON 

class Neuron(object): 
	def __init__(self,neuron_type,weight,id_number = 0): 
		self.type = neuron_type 
		self.id = id_number 
		self.th = THRESHOLD 	# threshold 
		self.lr = LEARNING_RATE 	# learning rate 
		self.w = weight # weight value axon
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
			if(self.is_type(TERMINAL)): 
				self.lightup() 
				self.hits += 1 
				self.lightdown() 
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
					#if self.learn(error)==-1: 
					#	return -1
					if(self.learn(error)==ERROR): 
						return ERROR 
					# sleep(0.05) 
					self.send(out) 

				if(self.learn(expected)==ERROR): 
					return ERROR 
				#self.send(out) 

	def learn(self,error): 
		correction = self.lr if (error==1) else -self.lr/2 
		self.w += correction # correct weight value based on error 
		if(self.w<=0.09):
			print self.w 
			return ERROR 
		return SUCCESS 

	def send(self,out): 
		self.lightup() 
		for synapse in self.axon: 
			synapse.lightup() 
			if(synapse.neuron_to.process(out)==ERROR): 
				synapse.erase() 
				if(synapse in self.axon): 
					self.axon.remove(synapse) 
			else: 
				synapse.reset() 
			synapse.lightdown() 
		self.lightdown() 

	def add_synapse(self,neuron): 
		syn = Synapse(self,neuron) 
		self.axon.append(syn) 
		return syn 

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


# color detectors for eye nerves/neurons 
class Cone(Neuron): 
	def __init__(self,neuron_type,weight,color_type,id_number = 0): 
		self.color_type = color_type 
		super(Cone,self).__init__(neuron_type,weight,id_number) 

	def send(self,out): 
		factor = 1.0/3.0
		self.lightup() 
		for synapse in self.axon: 
			synapse.lightup() 
			if(synapse.neuron_to.process(out*factor)==ERROR): 
				synapse.erase() 
				self.axon.remove(synapse) 
			else: 
				synapse.reset() 
			synapse.lightdown() 
		self.lightdown() 

	def lightup(self): 
		if self.color_type==RED: 
			color = color_rgb(220,100,100) 
		elif self.color_type==GRN: 
			color = color_rgb(100,220,100) 
		elif self.color_type==BLU: 
			color = color_rgb(100,100,220) 
		else: 
			color = color_rgb(220,220,100) 
		self.body.setFill(color) 

	def draw(self,win,x,y): 
		super(Cone,self).draw(win,x,y) 
		if self.color_type==RED: 
			color = color_rgb(150,0,0) 
		elif self.color_type==GRN: 
			color = color_rgb(0,150,0) 
		elif self.color_type==BLU: 
			color = color_rgb(0,0,150) 
		else: 
			color = color_rgb(100,100,0) 

		self.body.setOutline(color) 
