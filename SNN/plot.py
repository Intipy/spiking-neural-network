import matplotlib.pyplot as plt



def plot_neuron_behaviour(time, data, neuron_type, neuron_id, y_title):
    plt.plot(time,data)
    plt.title('{} @ {}'.format(neuron_type, neuron_id))
    plt.ylabel(y_title)
    plt.xlabel('Time (msec)')
    # Autoscale y-axis based on the data (is this needed??)
    y_min = 0
    y_max = max(data)*1.2
    if y_max == 0:
        y_max = 1
    plt.ylim([y_min,y_max])
    plt.show()



def plot_membrane_potential(time, Vm, neuron_type, neuron_id=0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title='Membrane potential (V)')



def plot_spikes(time, Vm, neuron_type, neuron_id=0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title='Spike (V)')



def plot_neuron_behaviour(time, data, neuron_type, neuron_id, y_title):
    print('Drawing graph with time.shape={}, data.shape={}'.format(time.shape, data.shape))
    plt.plot(time,data)
    plt.title('{} @ {}'.format(neuron_type, neuron_id))
    plt.ylabel(y_title)
    plt.xlabel('Time (msec)')
    # Graph to the data with some headroom...
    y_min = 0
    y_max = max(data)*1.2
    if y_max == 0:
        y_max = 1
    plt.ylim([y_min,y_max])
    plt.show()



def plot_membrane_potential(time, Vm, neuron_type, neuron_id = 0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title = 'Membrane potential (V)')



def plot_spikes(time, Vm, neuron_type, neuron_id = 0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title = 'Spike (V)')