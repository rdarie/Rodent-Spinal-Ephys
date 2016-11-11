from plot_sta import compare_sta
import numpy as np

input_chan = [0,1]
output_chan = ['CDP', 'trigger']

# try different preprocessing filters on the spikes
remove_mean = lambda x: x - np.mean(x, axis = 0)
baseline_subtract = lambda x: x - x[0]

compare_sta(input_chan, output_chan, 15, baseline_subtract, debugging = True,conditions = ['perlapine', 'severed'], override_ylim = 0)
#compare_sta(input_chan, output_chan, 15, baseline_subtract, debugging = True,conditions = ['control', 'lidocaine'])
