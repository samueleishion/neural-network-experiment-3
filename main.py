from pkg.graphics import * 
from pkg.utils import * 
# from bio.neuron import * 
from bio.organ import * 
from settings import * 

def main(): 
	# Testing individual neuron 
	# n = Neuron(0,.5,1) 
	# n.draw(win,50,50) 

	# Testing organ 
	# o = Organ(SENSORY_NEURONS)
	# o.draw(win,WINDOW_X/2,WINDOW_Y/4) 

	# Testing hand 
	h = Hand(SENSORY_NEURONS) 
	h.draw(win,WINDOW_X/4,WINDOW_Y/4) 

	# Testing eye 
	e = Eye(SENSORY_NEURONS) 
	e.draw(win,3*WINDOW_X/4,WINDOW_Y/4) 

	win.getMouse() 
	win.close() 

main()