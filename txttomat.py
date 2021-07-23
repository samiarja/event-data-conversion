'''
    Description: Convert .txt to .mat
    Requirements: make sure the .txt file is compressed .zip
'''

import numpy as np
import scipy.io as sio
from tqdm import tqdm
from util import Timer, Event, normalize_image, animate, load_events, plot_3d, event_slice

FILENAME = "/media/sami/Samsung_T5/MPhil/Dataset/RPG/poster_rotation/events.zip"
eventsarray = []

with Timer('Loading'):
    n_events = 15e6
    event_data = load_events(FILENAME, n_events)

events = event_data.event_list

for i, e in tqdm(enumerate(events)):
    event = -1*np.ones(4,dtype=np.uint64)
    event[0] = e.x
    event[1] = e.y
    event[2] = e.p
    event[3] = e.t
    eventsarray.append(event)
sio.savemat('/media/sami/Samsung_T5/MPhil/Dataset/mat/poster_rotation.mat',{'events':np.asarray(eventsarray)})
print("Converted succesfully to .mat")