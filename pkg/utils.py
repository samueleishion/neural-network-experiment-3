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