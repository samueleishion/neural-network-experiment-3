from pkg.graphics import * 
from bio.neuron import * 
from settings import * 

def main(): 
	win = GraphWin("Neural Network Graph",WINDOW_X,WINDOW_Y) 
	n = Neuron(0,.5,1)
	n.draw(win,50,50)

	win.getMouse() 
	win.close() 

main()