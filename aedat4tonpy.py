import glob, os
from dv import AedatFile
import numpy as np
import scipy.io as sio
from tqdm import tqdm
import cv2

'''
    convert from aedat4 to npy
'''

FILENAME = 'HIE-2020_03_09_15_37_00'
file_path = '/media/sami/Samsung_T5/MPhil/Dataset/HIE/aedat4/' + FILENAME + '.aedat4'
events = []

with AedatFile(file_path) as f:
    # list all the names of streams in the file
    print(f.names)
    
    for e in tqdm(f['events']):
        event = -1*np.ones(4,dtype=np.uint32)
        event[0] = e.x
        event[1] = e.y
        if e.polarity:
            event[2] = 1
        event[3] = e.timestamp
        events.append(event)
    np.save("/home/sami/sami/Dataset/data/test1/" + FILENAME + ".npy",events.astype('int32'))
    print(FILENAME + " Converted succesfully to .npy")


