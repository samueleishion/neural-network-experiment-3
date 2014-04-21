from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from data.report import * 
from bio.neuron import * 
from bio.organ import * 
from bio.network import * 
from settings import * 

def main(): 
	# Testing individual neuron 
	# n = Neuron(0,.5,1) 
	# n.draw(win,50,50) 

	# Testing organ 
	# o = Organ(SENSORY_NEURONS)
	# o.draw(win,WINDOW_X/2,WINDOW_Y/4) 

	# Testing hand 
	# h = Hand(SENSORY_NEURONS) 
	# h.draw(win,WINDOW_X/4,WINDOW_Y/4) 

	# Testing eye 
	# e = Eye(SENSORY_NEURONS) 
	# e.draw(win,3*WINDOW_X/4,WINDOW_Y/4) 

	# Testing network 
	n = Network() 
	h = Hand(SENSORY_NEURONS,1) 
	e = Eye(SENSORY_NEURONS,2) 
	l = Hand(SENSORY_NEURONS,3)
	n.add_organ(h) 
	n.add_organ(e) 
	n.add_organ(l) 
	n.draw(win) 

	r = Report(n) 
	if(GRAPH): 
		r.draw(win) 
	for neuron in n.terminals: 
		neuron.r = r 

	while(True): 
		if(AUTOMATIC): 
			i = 0 
			for organ in n.organs: 
				r.active_graph = i 
				for neuron in organ.neurons: 
					r.active_neuron = neuron.id 
					neuron.send(INTENSITY) 
				if(GRAPH): 
					r.update(i) 
				i += 1 

			for synapse in n.synapses: 
				if(synapse.live()==ERROR): 
					n.synapses.remove(synapse) 

		else: 
			click = get_click() 
			was_click_perceived(n,click[0],click[1]) 

	win.close() 

main()