from pkg.graphics import * 
from pkg.consts import * 
from pkg.utils import * 
from data.report import * 
# from bio.neuron import * 
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
	h = Hand(SENSORY_NEURONS) 
	l = Hand(SENSORY_NEURONS)
	e = Eye(SENSORY_NEURONS) 
	r = Report(n) 
	n.add_organ(h) 
	n.add_organ(e) 
	n.add_organ(l) 
	n.draw(win) 

	if(GRAPH): 
		r.draw(win) 

	while(True): 
		if(AUTOMATIC): 
			for organ in n.organs: 
				for neuron in organ.neurons: 
					neuron.send(INTENSITY) 
					# if(isinstance(neuron, Cone)): 
					# 	r = random.randint(0,INTENSITY) 
					# 	g = random.randint(0,INTENSITY) 
					# 	b = random.randint(0,INTENSITY) 
					# 	neuron.send(r,g,b) 
					# else: 
					# 	neuron.send(INTENSITY) 
			print "living synapses" 
			for synapse in n.synapses: 
				if(synapse.live()==ERROR): 
					n.synapses.remove(synapse) 

		else: 
			click = get_click() 
			was_click_perceived(n,click[0],click[1]) 

	win.close() 

main()