
# Pylake package that LUMICKS provides
import lumicks.pylake as pylake

# standard python toolkit for more elaborate mathematical operations
import numpy as np

# plotting library
import matplotlib.pyplot as plt

#############################################################################################
file= pylake.File('file directory/filename.h5')
# access the channel(s) we need

#point scan - photon counts in green and red channel
blue_data = file.blue_photon_count[:].data
green_data = file.green_photon_count[:].data   
red_data = file.red_photon_count[:].data

# time points
time_counts = file.green_photon_count[:].timestamps
time_counts = (time_counts - time_counts[0]) *1e-9   # times counts in seconds


# save the data as txt file: [time, blue counts, green counts, red counts]
all_photon_counts= np.vstack((time_counts,blue_data,green_data,red_data)).T
np.savetxt('file directory/filename.txt',all_photon_counts, 
           delimiter=',',header='time blue green red' )