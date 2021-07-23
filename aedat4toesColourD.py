'''
    Description: Convert .aedat4 format to .es using loris and pyDV
    using the colourDAVIS346
'''

import loris
import numpy as np
import matplotlib.pyplot as plt 
import os
import fnmatch
from tqdm import tqdm
from npy_to_matlab import npy_to_matlab
import scipy.io as sio
import glob, os
from dv import AedatFile
import matplotlib.pyplot as plt
import os

FILENAME = "bluebackgroundRedcircleLowlighttest"

parentFile = "/media/sami/Samsung_T5/MPhil/Dataset/aedat4/" + FILENAME + ".aedat4"
destinationFile = "/media/sami/Samsung_T5/MPhil/Dataset/es/"
events = []
with AedatFile(parentFile) as f:
    # list all the names of streams in the file
    print(FILENAME)
    print(f.names)
    
    for e in tqdm(f['events']):        
        event = np.zeros(4,dtype=np.uint32)
        event[0] = e.timestamp
        event[1] = e.x
        event[2] = e.y
        if e.polarity:
            event[3] = 1
        events.append(event)
        
finalArray = np.asarray(events)
finalArray[:,0] -= finalArray[0,0]
ordering = "txyp"
loris.write_events_to_file(finalArray, destinationFile + FILENAME + ".es",ordering)
print("File: " + FILENAME + "converted to .es")