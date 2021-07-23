import glob, os
from dv import AedatFile
import numpy as np
import scipy.io as sio
from tqdm import tqdm
import cv2

'''
    convert from aedat4 to mat
'''

FILENAME = 'HIE-2020_03_09_15_47_53'
file_path = '/media/sami/Samsung_T5/MPhil/Dataset/HIE/aedat4/' + FILENAME + '.aedat4'
events = []

with AedatFile(file_path) as f:
    # list all the names of streams in the file
    print(f.names)
    
    for e in tqdm(f['imu']):
        cameraMotion        = -1*np.ones(6,dtype=np.uint32)
        cameraMotion[0]     = e.accelerometer[0]
        cameraMotion[1]     = e.accelerometer[1]
        cameraMotion[2]     = e.accelerometer[2]
        cameraMotion[0]     = e.gyroscope[0]
        cameraMotion[1]     = e.gyroscope[1]
        cameraMotion[2]     = e.gyroscope[2]
        events.append(cameraMotion)
        
    sio.savemat('/media/sami/Samsung_T5/MPhil/Dataset/HIE/mat/' + FILENAME + 'AccGyro.mat',{'events':np.asarray(events)})
    print(FILENAME + " Converted succesfully...")

