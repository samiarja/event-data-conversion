import loris
import numpy as np
import matplotlib.pyplot as plt 
import os
import fnmatch
from tqdm import tqdm
from npy_to_matlab import npy_to_matlab
import scipy.io as sio

Recording_Number = 5
colorEventCountArrayFinal = []

FILENAME = "bluebackgroundRedcircleLowlighttest"
# RealSignalWhitebackgroundGreenCircle            
# RealSignalWhitebackgroundBlueCircle
# RealSignalWhitebackgroundRedCircle
# RealSignalGreenbackgroundBlueCircle
# RealSignalGreenbackgroundRedCircle (not this)
# RealSignalBluebackgroundGreenCircle (not this)
# RealSignalBluebackgroundRedCircle
# RealSignalRedbackgroundGreenCircle
# RealSignalRedbackgroundBlueCircle

myPath = "/media/sami/Samsung_T5/MPhil/Dataset/es/"
destinationPath = "/media/sami/Samsung_T5/MPhil/Dataset/mat/"
# myPath = "/home/sami/sami/Dataset/colour/testes/"
# myPath = "../davis346_recorder/recordings/coloursignature/1/"

# countESFile = len(fnmatch.filter(os.listdir(myPath), '*.es'))

# for filesDir in tqdm(range(countESFile)):
# FILENAME = os.listdir('/home/sami/sami/Dataset/colour/testes/')[filesDir]
# print(FILENAME + "file being converted...")
my_file = loris.read_file(myPath + FILENAME + ".es")
events = my_file['events']
matT = my_file['events'].ts
matX = my_file['events'].x
matY = my_file['events'].y
matP = my_file['events'].p
matC = np.zeros((events.shape[0],1))
nEvents = matT.shape[0]
events = np.zeros((nEvents,4))
events[:,0] = matT.flatten()
events[:,1] = matX.flatten()
events[:,2] = matY.flatten()
events[:,3] = matP.flatten()

# for idx in range(len(events[:,1])):
#     # if events[idx,1] > 50 and events[idx,1] < 300 and events[idx,2] > 90 and events[idx,2] < 200:
#     if events[idx,1] % 2 == 0 and events[idx,2] % 2 != 0: # X even and Y odd (Bottom right)
#         matC[idx] = 1 # (Blue)
#     if events[idx,1] % 2 != 0 and events[idx,2] % 2 == 0: # X odd and Y even (Top left)
#         matC[idx] = 2  # (Red)
#     if events[idx,1] % 2 == 0 and events[idx,2] % 2 == 0: # X even and Y even (Top right)
#         matC[idx] = 3 # (Green1)
#     if events[idx,1] % 2 != 0 and events[idx,2] % 2 != 0: # X odd and Y odd (Bottom left)
#         matC[idx] = 4 # (Green2)
# events = np.hstack((events,matC))
# # np.save(destinationPath + str(filesDir) + ".npy",events.astype('int32'))

#### ONLY USE THIS PIXEL LABELLING, THIS IS THE CORRECT ONE
for idx in range(len(events[:,1])):
    # if events[idx,1] > 50 and events[idx,1] < 300 and events[idx,2] > 90 and events[idx,2] < 200:
    if events[idx,1] % 2 != 0 and events[idx,2] % 2 != 0: # X even and Y odd (Bottom right)
        matC[idx] = 1 # (Blue)
    if events[idx,1] % 2 == 0 and events[idx,2] % 2 == 0: # X odd and Y even (Top left)
        matC[idx] = 2  # (Red)
    if events[idx,1] % 2 == 0 and events[idx,2] % 2 != 0: # X even and Y even (Top right)
        matC[idx] = 3 # (Green1)
    if events[idx,1] % 2 != 0 and events[idx,2] % 2 == 0: # X odd and Y odd (Bottom left)
        matC[idx] = 4 # (Green2)
events = np.hstack((events,matC))
# np.save(destinationPath + str(filesDir) + ".npy",events.astype('int32'))

sio.savemat(destinationPath +  FILENAME + ".mat",{'events':np.asarray(events)})
print(FILENAME + " file saved")

# for filesDir in tqdm(range(countESFile)):
#     my_file = np.load(destinationPath + str(filesDir) + ".npy")
#     npy_to_matlab.py(my_file)
#     print("converted")