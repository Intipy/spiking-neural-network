import numpy as np
import matplotlib.pyplot as plt
import random
import SNN



T = 10  # total time to sumulate (msec)
dt = 0.0125  # Simulation timestep
time = int(T / dt)
inpt = 1.0  # Neuron input voltage
neuron_input = np.full(time, inpt)



neurons = SNN.model.create_neurons(num_layers=2, num_neurons=100, debug=False)



stimulus_len = len(neuron_input)
layer = 0
for neuron in range(100):
    offset = random.randint(0, 100)   # Simulates stimulus starting at different times
    stimulus = np.zeros_like(neuron_input)
    stimulus[offset:stimulus_len] = neuron_input[0:stimulus_len - offset]
    neurons[layer][neuron].spike_generator(stimulus)



layer_spikes = np.zeros_like(neurons[0][0].spikes)
for i in range(100):
    layer_spikes += neurons[0][i].spikes
print(layer_spikes[0:200])



neurons[1][0] = SNN.neuron.LIF(debug=False)           # Re-initialise this neuron in case of multiple runs
neurons[1][0].spike_generator(layer_spikes)



start_time = 0
end_time = len(neurons[1][0].time)



SNN.plot.plot_membrane_potential(neurons[0][0].time, neurons[0][0].Vm, 'Membrane Potential {}'.format(neurons[0][0].type), neuron_id ="0/0")
SNN.plot.plot_spikes(neurons[0][0].time, neurons[0][0].spikes, 'Output spikes for {}'.format(neurons[0][0].type), neuron_id ="0/0")
SNN.plot.plot_spikes(neurons[0][0].time, layer_spikes, 'Output spikes for layer {}'.format(layer))


SNN.plot.plot_spikes(neurons[0][0].time[start_time:end_time], layer_spikes[start_time:end_time], 'Input Spikes for {}'.format(neurons[1][0].type), neuron_id ="1/0")
SNN.plot.plot_membrane_potential(neurons[1][0].time[start_time:end_time], neurons[1][0].Vm[start_time:end_time], 'Membrane Potential {}'.format(neurons[1][0].type), neuron_id ="1/0")
SNN.plot.plot_spikes(neurons[1][0].time[start_time:end_time], neurons[1][0].spikes[start_time:end_time], 'Output spikes for {}'.format(neurons[1][0].type), neuron_id ="1/0")


