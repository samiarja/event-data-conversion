import os
import numpy as np
import matplotlib.pyplot as plt
from dv import LegacyAedatFile
import scipy.io as sio
from tqdm import tqdm

'''
    convert from aedat4 to mat for DVS gesture Dataset
'''

initialDataset = os.listdir('/media/sami/Samsung_T5/MPhil/Dataset/gestureDVS/onlyaedat/')
for idx in range(1,len(initialDataset)):
    FILENAME = initialDataset[idx]
    print(FILENAME)
    filename = '/media/sami/Samsung_T5/MPhil/Dataset/gestureDVS/onlyaedat/' + FILENAME
    events = []

    def readAedatEvent(filename):
        xEvent = []
        yEvent = []
        pEvent = []
        tEvent = []
        with LegacyAedatFile(filename) as f:
            for event in tqdm(f):
                xEvent.append(event.x)
                yEvent.append(event.y)
                pEvent.append(event.polarity)
                tEvent.append(event.timestamp)
        events = [xEvent, yEvent, pEvent, tEvent]

        sio.savemat('/media/sami/Samsung_T5/MPhil/Dataset/gestureDVS/mat/' + FILENAME + '.mat',
                    {'events': np.asarray(events)})
        print(FILENAME + " Converted succesfully to .mat")
        return xEvent, yEvent, pEvent, tEvent

    readAedatEvent(filename)
