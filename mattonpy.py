from scipy.io import loadmat
import numpy as np
mat = loadmat("/home/sami/sami/Dataset/data/test2/test2.mat")

for k, v in (mat.items()):
    if 'TD' in k:
                    matTD = mat['TD']
                    matX = mat['TD'][:,0]
                    matY = mat['TD'][:,1]
                    matP = mat['TD'][:,2]
                    matT = mat['TD'][:,3].astype('int32')
                    nEvents = matT.shape[0]
                    events = np.zeros((nEvents,4))

                    events[:,0] = matX.flatten()
                    events[:,1] = matY.flatten()
                    events[:,3] = matT.flatten()
                    events[:,2] = matP.flatten()

                    np.save("/home/sami/sami/Dataset/data/test1/test1.npy",events.astype('int32'))
                    
    elif 'events' in k:
                    matTD = mat['events']
                    matX = mat['events'][:,0]
                    matY = mat['events'][:,1]
                    matP = mat['events'][:,2]
                    matT = mat['events'][:,3].astype('int32')
                    nEvents = matT.shape[0]
                    events = np.zeros((nEvents,4))

                    events[:,0] = matX.flatten()
                    events[:,1] = matY.flatten()
                    events[:,3] = matT.flatten()
                    events[:,2] = matP.flatten()

                    np.save("/home/sami/sami/Dataset/data/test1/test1.npy",events.astype('int32'))