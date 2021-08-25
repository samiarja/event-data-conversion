import loris
import numpy as np
import matplotlib.pyplot as plt 
import os
import fnmatch
from tqdm import tqdm
import scipy.io as sio

# FILENAME = "threeSmallCirclesData-2021_01_12_12_16_33_WithColourLabelsTD"
# mat = sio.loadmat('/home/sami/sami/Dataset/mat/' + FILENAME + '.mat')

# FILENAME = "redbackgroundgreencircleTD"
# mat = sio.loadmat('/media/sami/Samsung_T5/MPhil/Dataset/mat/' + FILENAME + '.mat')

FILENAME = "other gestures"
mat = sio.loadmat('/media/sami/Samsung_T5/MPhil/Code/DeepGreen/gestureDVS/classifiedGestures/' + FILENAME + '.mat')

events = []


matX =  mat['TD'][0][0][0]
matY =  mat['TD'][0][0][1]
matP =  mat['TD'][0][0][2]
matTs = mat['TD'][0][0][3]

# matP[matP == -1] = 0 # only if the polarity is -1 and 1

nEvents = matX.shape[0]
events = np.zeros((nEvents,4))

events = np.concatenate((matTs,matX, matY, matP),axis=1).reshape((nEvents,4))

# print(events.shape[0])

finalArray = np.asarray(events)
finalArray[:,0] -= finalArray[0,0]

ordering = "txyp"
loris.write_events_to_file(finalArray, "/media/sami/Samsung_T5/MPhil/Dataset/es/" + FILENAME + ".es",ordering)
print("File: " + FILENAME + "converted to .es")


# my_file = loris.read_file(mat)
# events = mat['finalPredictedEvents']
# matT = mat['finalPredictedEvents'][3]
# matX = mat['finalPredictedEvents'][0]
# matY = mat['finalPredictedEvents'][1]
# matP = mat['finalPredictedEvents'][2]

# print(mat)

# print(mat['finalPredictedEvents'][0][0][0][0])