from SNN import neuron



def create_neurons(num_layers=0, num_neurons=0, debug=True):
    neurons = []
    for layer in range(num_layers):
        if debug:
            print ('create_neurons(): Creating layer {}'.format(layer))
        neuron_layer = []
        for count in range(num_neurons):
            neuron_layer.append(neuron.LIF(debug=debug))
        neurons.append(neuron_layer)
    return neurons