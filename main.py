from pkg.graphics import * 
from pkg.utils import * 
from bio.neuron import * 
from settings import * 

def main(): 
	n = Neuron(0,.5,1) 
	n.draw(win,50,50) 

	win.getMouse() 
	win.close() 

main()