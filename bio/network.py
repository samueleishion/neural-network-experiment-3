from settings import * 
from pkg.utils import * 
from bio.network import * 
from bio.neuron import * 
import random 

class Network: 
	def __init__(self): 
		self.organs = [] 
		self.transmitters = [] 
		self.terminals = [] 

		for i in range(TERMINAL_NEURONS): 
			self.terminals.append(create_neuron(TERMINAL)) 

	def add_organ(self,organ):
		# generate organ's neurons' transmitters 
		temp = []
		for i in range(SENSORY_NEURONS+TERMINAL_NEURONS): 
			n = create_neuron(TRANSMITTER) 
			temp.append(n) 

		# connecting organ's sensorial neurons with transmitters 
		for neuron in organ.neurons: 
			for synapse in temp: 
				rand = random.randint(0,5) 
				if(rand==0): 
					neuron.add_synapse(synapse) 

		# connecting transmitters with other transmitters  
		for neuron in temp: 
			for other in temp: 
				#rand = random.randint(0,40) if neuron==other else random.randint(0,100) 
				if(neuron==other): 
					continue 
				else: 
					rand = random.randint(0,50) 
				if(rand==0): 
					neuron.add_synapse(other) 

		# conencting transmitters with terminals 
		for neuron in temp: 
			for terminal in self.terminals: 
				rand = random.randint(0,7) 
				if(rand==0): 
					neuron.add_synapse(terminal) 

		# storing organ and transmitters on network 
		self.organs.append(organ) 
		self.transmitters.append(temp) 

	def draw(self,win): 
		organs_num = len(self.organs) 
		organs_space = WINDOW_X/organs_num 

		# drawing organs 
		i = 0 
		for organ in self.organs: 
			x = (organs_space*i)+(organs_space/4) 
			y = 50 
			organ.draw(win,x,y) 
			i += 1 

		# drawing transmitters 
		i = 0 
		for transmitter in self.transmitters: 
			for neuron in transmitter: 
				x = ((organs_space*i)+50)+random.randint(0,organs_space-150) 
				y = 150+random.randint(0,WINDOW_Y-300) 
				neuron.draw(win,x,y) 
			i += 1

		# drawing terminals 
		i = 0 
		for terminal in self.terminals: 
			x = (WINDOW_X/2)-(len(self.terminals)*(NEURON_SIZE*1.5))+(((NEURON_SIZE*2)+5)*i) 
			y = WINDOW_Y-50 
			terminal.draw(win,x,y) 
			i += 1 

		# drawing connections between organs' sensory neurons and transmitters 
		i = 0
		for organ in self.organs: 
			for neuron in organ.neurons: 
				p1 = neuron.body.getCenter() 
				for synapse in neuron.axon: 
					p2 = synapse.body.getCenter() 
					line = Line(p1,p2)
					line.setFill(color_rgb(200,200,200))
					line.draw(win) 
			i += 1 

		# drawing connections between transmitters and terminal neurons 
		for transmitter in self.transmitters: 
			for neuron in transmitter: 
				p1 = neuron.body.getCenter() 
				for synapse in neuron.axon: 
					p2 = synapse.body.getCenter() 
					line = Line(p1,p2) 
					line.setFill(color_rgb(200,200,200)) 
					line.draw(win) 


