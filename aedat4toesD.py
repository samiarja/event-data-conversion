'''
    Description: Convert .aedat4 format to .es using loris and pyDV
    using DAVIS346 mono
'''

import loris
import numpy as np
import matplotlib.pyplot as plt 
import os
import fnmatch
from tqdm import tqdm
import scipy.io as sio
import glob, os
from dv import AedatFile
import matplotlib.pyplot as plt

# FILENAME = "REGULARDAVIS-2020_08_26_15_11_18.aedat4"
# parentFile = "/home/sami/sami/Dataset/aedat4/" + FILENAME

FILENAME = "data5-2021_01_27_12_39_59"
parentFile = "/home/sami/sami/Dataset/aedat4/" + FILENAME + ".aedat4"
# parentFile = "../pixelShift/" + FILENAME + ".aedat4"

my_file = loris.read_file(parentFile)

my_file["events"]["ts"] -= my_file["events"]["ts"][0]
loris.write_events_to_file(my_file["events"], "/home/sami/sami/Dataset/es/" + FILENAME + ".es")
print("File:",FILENAME,"is successfully converted to .es format")
