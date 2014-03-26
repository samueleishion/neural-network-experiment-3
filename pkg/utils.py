from settings import * 
from graphics import * 
from bio.neuron import * 
import random 

SENSORIAL 	= 0
TRANSMITTER = 1 
TERMINAL 	= 2 
MOTOR 		= 3 

win = GraphWin("Neural Network Graph",WINDOW_X,WINDOW_Y) 

def flip(n):
	return 1 if n==0 else 0 

def create_neuron(neuron_type): 
	weight = 0 
	while(weight==0 or weight==1):
		weight = random.uniform(0.0,1.0) 
	return Neuron(neuron_type,weight) 

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
			# else:
			# 	if(i==1):
			# 		print str(x)+" e ["+str(nx-nr)+","+str(nx+nr)+"] ", 
			# 		print str(y)+" e ["+str(ny-nr)+","+str(ny+nr)+"]"
		i += 1 

	print "not found"
	return False 