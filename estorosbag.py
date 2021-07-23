## First method
# import subprocess, yaml
# info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', '/home/sami/sami/Dataset/bag/calib_outdoor_infrared.bag'], stdout=subprocess.PIPE).communicate()[0])
# print(info_dict)

# import rosbag
# bag = rosbag.Bag('/home/sami/sami/Dataset/bag/calib_outdoor_infrared.bag')
# topics = bag.get_type_and_topic_info()[1].keys()
# types = []
# for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
#     types.append(bag.get_type_and_topic_info()[1].values()[i][0])
                 
# # Second method equivalent
# import rosbag
# bag = rosbag.Bag('/home/sami/sami/Dataset/bag/calib_outdoor_infrared.bag')
# for topic, msg, t in bag.read_messages(topics=['/dvs/events']):
#     print("ts:", msg.events[0].ts, "x:", msg.events[0].x, "y:", msg.events[0].y, "p:", msg.events[0].polarity)
#     # print(msg.events[0].x)
#     # print(msg.events[0].y)
#     # print(msg.events[0].polarity)
#     # print(msg.events[0].ts)
# bag.close()

import rosbag
import loris
import numpy as np
from std_msgs.msg import Int32, String

FILEPATH = "/home/sami/sami/Dataset/es/HIE-2020_03_09_15_48_39.aedat4.es"
bag = rosbag.Bag('test.bag', 'w')

try:
    my_file = loris.read_file(FILEPATH)
    events = my_file['events']
    for event in events:
        
        i = Int32()
        i.data = event.x
        bag.write('/dvs/events', i)
        # e = np.zeros(4,dtype=np.uint32)
        # # print("ts:", event.t, "x:", event.x, "y:", event.y, "p:", event.p)
        # event[0] = event.t
        # e[1] = event.x
        # e[2] = event.y
        # if event.p:
        #     e[3] = 1
        # EventArray.append(e)
        
    # finalArray = np.asarray(EventArray)
    # finalArray[:,0] -= finalArray[0,0]
  
    
finally:
    bag.close()