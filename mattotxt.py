import math
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

path_to_events = sio.loadmat("/media/sami/USB DISK/mat/labeller/Today/RGB-FEAST.mat")
path_to_events = sio.loadmat("/home/sami/sami/Dataset/HIE/mat/dvSave-2020_02_21_12_58_55.mat")
path_to_events = sio.loadmat("/home/sami/sami/Code/DeepGreen/greenhouseCode/recordings/new_data/newDataToday-2020_06_03_17_08_06.mat")

matX = path_to_events['events'][:,0]
matY = path_to_events['events'][:,1]
matP = path_to_events['events'][:,2]
matT = path_to_events['events'][:,3].astype('int64')

nEvents = matT.shape[0]
events = np.zeros((nEvents,4))
events[:,0] = matT.flatten()
events[:,1] = matX.flatten()
events[:,2] = matY.flatten()
events[:,3] = matP.flatten()

events[0,0] = 0
events[0,1] = 0
events[0,2] = 346
events[0,3] = 260

print(events.shape)
np.savetxt("newDataToday-2020_06_03_17_08_06.txt",events.astype('int64'), delimiter=' ', fmt='%s')