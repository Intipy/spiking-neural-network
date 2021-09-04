from SNN import neuron



def create_neurons(num_layers, num_neurons, debug=True):
    neurons = []
    for layer in range(num_layers):
        if debug:
            print ('create_neurons(): Creating layer {}'.format(layer))
        neuron_layer = []
        for count in range(num_neurons):
            neuron_layer.append(neuron.LIFNeuron(debug=debug))
        neurons.append(neuron_layer)
    return neurons