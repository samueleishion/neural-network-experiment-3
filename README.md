Neural Network Experiment 3
===========================

A visual representation of a simple neural network expanding on previous work done on https://github.com/samueleishion/neural-network-experiment-2

How to run it
-------------
```
make network 
```

Please note this version of the experiment is designed for Python 2.* 

To clean the project: 
``` 
make clean
``` 

How to interact
---------------
Several nodes (neurons) will be displayed. The top ones are sensorial, the middle ones are transmitters, and the bottom ones are terminals. There are also groups of sensorial neurons that compose hands (left/right) and an eye (center). The eye sensory neurons is composed by 3 cones that (will) detect color (red, green, and blue). 

On the bottom of the graphic window, there is a graph/map-like visualization of the interactions between sensorial and terminal neurons. The sensorial neurons are displayed on the y-axis while the terminal neurons are displayed on the x-axis. Each graph/map is aligned vertically with its correspondent organ. 

Several features can be changed to change the experiment on the settings.py file. The features include: 

#### Number of neurons 
``` 
SENSORY_NEURONS = 10 
``` 
* purpose: establishes total number of sensorial neurons 
* type: int 
* default value: 10 

``` 
TERMINAL_NEURONS = 10 
```
* purpose: establishes total number of terminal neurons 
* type: int 
* default value: 10 

#### Sensation intensity 
``` 
INTENSITY = 1 
``` 
* purpose: equivalent to duration/potence of sensation, this is a fixed number for all sensations in this experiment 
* type: int 
* default value: 1 

#### Automatic and monitored interaction 
``` 
AUTOMATIC = True 
``` 
* purpose: allows the sensations to be automatically distributed 
* type: boolean 
* default value: True
* detail: setting this feature to `True` facilitates the graph visualization and experimentation 

```
GRAPH = True 
``` 
* purpose: displays the right panel with the graph/map-like visualization 
* type: boolean 
* default value: True 
* detail: this graph maps the number of reached terminals after trigerring a given sensory neuron. 
 
Visualization
-------------
If the `GRAPH` feature is set to `True`, the y-axis represents the sensorial neurons. The x-axis represents the sensorial neurons. If a given sensory neuron (S) has sent a transmission and is received by a given terminal neuron (T), then the graph at coordinates (S,T) will be lit up with a shade of red (given that, for this particular graphics window the y-axis increases downwards). 

For example, we have 3 sensory neurons and 4 terminal neurons. This would be a numeric representation of the graph: 

|    | T1 | T2 | T3 | T4 | 
| ---- |:-------------:|:-------------:|:-------------:|:-------------:|
| **S1** | 0 | 0 | 0 | 0 |
| **S2** | 0 | 0 | 0 | 0 |
| **S3** | 0 | 0 | 0 | 0 | 

After several interactions, say that: 
* S1 has successfully transmitted 
  * 3 sensations to T1
  * 2 sensations to T2
* S2 has successfully transmitted 
  * 1 sensation to T2
  * 3 sensations to T3 
  * 2 sensations to T4 
* S3 has successfully transmitted 
  * 2 sensations to T1 
  * 4 sensations to T3
  * 1 sensation to T4 

Our graph will now be: 

|    | T1 | T2 | T3 | T4 | 
| ---- |:-------------:|:-------------:|:-------------:|:-------------:|
| **S1** | .6 | .4 | 0 | 0 |
| **S2** | 0 | .17 | .5 | .33 |
| **S3** | .29 | 0 | .57 | .14 | 

On the actual visualization, these decimals are used to calculate the intensity of the color. 