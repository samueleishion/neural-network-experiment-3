from graphics import * 
from settings import *

SENSORIAL 	= 0
TRANSMITTER = 1 
TERMINAL 	= 2 
MOTOR 		= 3 

RED 	= 0
GRN 	= 1
BLU 	= 2 

WINDOW_X = 1000 		# Sets window horizontal dimension 
WINDOW_Y = 700 			# Sets window vertical dimension 
NEURON_SIZE = 10 		# Sets radius of each neuron 

NEURON_COUNT = 0 

ERROR = -1 
NULL = 0 
SUCCESS = 1 

THRESHOLD = 0.5 
LEARNING_RATE = 0.2 
SYNAPSE_LIFESPAN = 20 

win = GraphWin("Neural Network Graph",WINDOW_X,WINDOW_Y) 