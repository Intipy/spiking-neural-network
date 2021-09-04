import numpy as np
import matplotlib.pyplot as plt
import random
import SNN



T = 10  # total time to sumulate (msec)
dt = 0.0125  # Simulation timestep
time = int(T / dt)
inpt = 1.0  # Neuron input voltage
neuron_input = np.full((time), inpt)
num_layers = 2
num_neurons = 100



neurons = SNN.model.create_neurons(num_layers, num_neurons, debug=False)



stimulus_len = len(neuron_input)
layer = 0
for neuron in range(num_neurons):
    offset = random.randint(0,100)   # Simulates stimulus starting at different times
    stimulus = np.zeros_like(neuron_input)
    stimulus[offset:stimulus_len] = neuron_input[0:stimulus_len - offset]
    neurons[layer][neuron].spike_generator(stimulus)



SNN.graph.plot_membrane_potential(neurons[0][0].time, neurons[0][0].Vm, 'Membrane Potential {}'.format(neurons[0][0].type), neuron_id ="0/0")
SNN.graph.plot_spikes(neurons[0][0].time, neurons[0][0].spikes, 'Output spikes for {}'.format(neurons[0][0].type), neuron_id ="0/0")



layer = 0
layer_spikes = np.zeros_like(neurons[layer][0].spikes)
for i in range(num_neurons):
    layer_spikes += neurons[layer][i].spikes



SNN.graph.plot_spikes(neurons[0][0].time, layer_spikes, 'Output spikes for layer {}'.format(layer))



print(layer_spikes[0:200])