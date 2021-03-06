from io_code import TDMS_to_dict
import pdb
import warnings

from Tkinter import Tk
from tkFileDialog import askopenfilename
from matplotlib import pyplot as plt

# get filename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
TDMS_filename = askopenfilename(initialdir = 'A:\\Reversible lesions\\Rodent Spinal Virus Transfection') # open window to get file name

if not TDMS_filename: # if file not selected, select a default
    TDMS_filename = 'A:\\Reversible lesions\Rodent Spinal Virus Transfection\\#4 - 20160615\\20160615_#4_HReflex_I0500_PW0025_A065_01.tdms'
    warning_string = "No file selected, setting to default: %s" % TDMS_filename
    warnings.warn(warning_string, UserWarning, stacklevel=2)

raw = TDMS_to_dict(TDMS_filename,[2,1],['Raw Voltage', 'trigger'])

pdb.set_trace()
plt.plot(1e3*raw['Raw Voltage']['time'], raw['Raw Voltage']['data'],'b-',label = 'Raw Voltage')
#plt.plot(1e3*raw['trigger']['time'], raw['trigger']['data'],'r-', label = 'TTL')

plt.legend(loc='upper left')
plt.xlabel('Time (msec)')
plt.ylabel('Voltage (V)')
plt.show()
