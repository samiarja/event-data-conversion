import glob, os
from dv import AedatFile
import numpy as np
import scipy.io as sio
from tqdm import tqdm
import cv2

'''
    convert from aedat4 to mat
'''

FILENAME = 'user01_fluorescent'
file_path = '/media/sami/Samsung_T5/MPhil/Dataset/gestureDVS/aedat4/' + FILENAME + '.aedat4'
events = []

with AedatFile(file_path) as f:
    print(f.names)
    
    for e in tqdm(f['events']):
        # print(e.timestamp)
        
        event = -1*np.ones(4,dtype=np.uint16)
        event[0] = e.x
        event[1] = e.y
        if e.polarity:
            event[2] = 1
        event[3] = e.timestamp
        events.append(event)
    sio.savemat('/media/sami/Samsung_T5/MPhil/Dataset/gestureDVS/mat/' + FILENAME + 'test.mat',{'events':np.asarray(events)})
    print(FILENAME + " Converted succesfully to .mat")
