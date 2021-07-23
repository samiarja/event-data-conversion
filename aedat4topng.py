from dv import AedatFile
import numpy as np
import scipy.io as sio
from tqdm import tqdm
import cv2
from PIL import Image
import os
import matplotlib.pyplot as plt
import subprocess

# HIE-2020_03_09_15_48_39
# HIE-2020_03_09_15_49_59
# HIE-2020_03_09_15_47_06
# HIE-2020_03_09_15_47_53
# HIE-2020_03_09_15_40_36
# HIE-2020_03_09_15_37_00
# HIE-2020_03_09_15_39_42
# HIE-2020_03_09_15_36_02
# HIE-2020_03_09_15_30_48
# HIE-2020_03_09_15_28_43

video = []
FILENAME = "HIE-2020_03_09_15_28_43"
initalPath = '/media/sami/Samsung_T5/MPhil/Dataset/HIE/aedat4/' + FILENAME + ".aedat4"
destinationPath = "/media/sami/Samsung_T5/MPhil/Dataset/HIE/"
framePath = "/media/sami/Samsung_T5/MPhil/Dataset/HIE/frames/"
vidsPath = "/media/sami/Samsung_T5/MPhil/Dataset/HIE/vids/"

with AedatFile(initalPath) as f:
    print(f.names)
    for e in tqdm(f['frames']):
        video3D = video.append(e.image,)
for i, j in zip(video, range(len(video))):
    I = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    rescaled = Image.fromarray(I)
    rescaled.save(
        destinationPath + "frames/%01d" % j + ".png")
os.system(
    "ffmpeg -f image2 -framerate 10 -i " + framePath + "%01d.png -vcodec libx264 -crf 22 " + vidsPath + FILENAME +".mp4")
print("Frames are successfully converted to .mp4")
frameslist = [ f for f in os.listdir(framePath) if f.endswith(".png") ]
for f in frameslist:
    os.remove(os.path.join(framePath, f))
print("Frames are deleted from framePath")
print(FILENAME + " file is converted to png then to .mp4")