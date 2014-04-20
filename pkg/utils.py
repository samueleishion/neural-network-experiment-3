from settings import * 
from consts import * 
from graphics import * 
from bio.neuron import * 
import random 

def flip(n):
	return 1 if n==0 else 0 

def create_neuron(neuron_type): 
	global NEURON_COUNT 
	NEURON_COUNT += 1
	weight = 0 
	while(weight==0 or weight==1):
		weight = random.uniform(0.0,1.0) 
	return Neuron(neuron_type,weight,NEURON_COUNT) 

def get_click(): 
	click = win.getMouse() 
	x = click.getX()
	y = click.getY()
	Point(x,y).draw(win) 
	return x,y 

def was_click_perceived(network,x,y): 
	i = 0
	for organ in network.organs: 
		print "checking "+str(i)+" ",
		print organ 
		for neuron in organ.neurons: 
			nr = neuron.body.getRadius() 
			nx, ny = neuron.get_coords() 

			if(( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )): 
				if(neuron.is_type(SENSORIAL)): 
					# print "sensed"
					neuron.process(INTENSITY) 
					print "found" 
					return True 
		i += 1 

	print "not found"
	return False 