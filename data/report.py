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
		self.active_graph = -1 
		self.active_neuron = -1 

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
		x_offset = 50 
		for graph in self.graphs: 
			graph.draw(win,x_offset,WINDOW_Y-200,190/SENSORY_NEURONS) 
			x_offset += space/3 

	def hit(self,neuron_hit): 
		if(self.active_graph!=ERROR and self.active_neuron!=ERROR): 
			self.graphs[self.active_graph].matrix[self.active_neuron][neuron_hit] += 1 
			# print "Updating graphs["+str(self.active_graph)+"].matrix["+str(self.active_neuron)+"]["+str(neuron_hit)+"] = "+str(self.graphs[self.active_graph].matrix[self.active_neuron][neuron_hit])

	def update(self,i): 
		# global mapped_hits 
		# total_hits = 0 
		# for terminal in self.network.terminals: 
		# 	total_hits += terminal.hits 
		# 	terminal.hits = 0 

		# for hit in mapped_hits: 
		# 	if hit.id in self.graphs[i].matrix: 
		# 		self.graphs[i].matrix[hit.id] = mapped_hits[hit]/total_hits 
		self.graphs[i].update() 


class Graph: 
	def __init__(self,organ_id): 
		self.id = organ_id 
		# self.matrix = [[0]*TERMINAL_NEURONS]*SENSORY_NEURONS 
		# self.rects = [[None]*TERMINAL_NEURONS]*SENSORY_NEURONS 
		self.matrix = [] 
		self.rects = [] 

		for s in range(SENSORY_NEURONS): 
			self.matrix.append([]) 
			self.rects.append([]) 
			for t in range(TERMINAL_NEURONS): 
				self.matrix[s].append(0) 
				self.rects[s].append(None) 


	def draw(self,win,left,top,size): 
		y = top  
		for row in range(len(self.rects)): 
			x = left 
			for col in range(len(self.rects[row])): 
				r = Rectangle(Point(x,y),Point(x+size,y+size)) 
				r.setFill(color_rgb(255,255,255)) 
				r.draw(win) 
				self.rects[row][col] = r # assign to rects at [row][col] 
				x += size 
			y += size 

	def update(self): 
		# for row in range(len(self.matrix)): 
		# 	for col in range(len(self.matrix[row])): 
		# 		gb = 255*self.matrix[row][col] 
		# 		self.rects[row][col].setFill(color_rgb(255,gb,gb)) 
		for sens in range(len(self.matrix)): 
			subtotal = 0 
			# print "["+str(sens)+"]" 
			for term in range(len(self.matrix[sens])): 
				# print "\t["+str(term)+"] : "+str(self.matrix[sens][term]) 
				subtotal += self.matrix[sens][term] 
			# print "\ttotal: "+str(subtotal)

			total = 0 
			for term in range(len(self.matrix[sens])): 
				total = self.matrix[sens][term]*1.0/subtotal if subtotal>0 else 0 
				gb = 255-(255*total) 
				self.rects[sens][term].setFill(color_rgb(255,gb,gb)) 
