from settings import * 
from graphics import * 

SENSORIAL 	= 0
TRANSMITTER = 1 
TERMINAL 	= 2 
MOTOR 		= 3 

win = GraphWin("Neural Network Graph",WINDOW_X,WINDOW_Y) 

def flip(n):
	return 1 if n==0 else 0 