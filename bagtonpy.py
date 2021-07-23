import sys
assert sys.version_info[0] == 2
import rosbag
import numpy as np
from rospy_message_converter import message_converter

bag = rosbag.Bag('out.bag')
nb_event = 0
x_fin = []
y_fin = []
ts_fin = []
p_fin = []
for topic, msg, t in bag.read_messages(topics=['/cam0/events']):
    msg_str = message_converter.convert_ros_message_to_dictionary(msg)
    events = msg_str['events']
    x = np.zeros(len(events), dtype=np.uint16)
    y = np.zeros(len(events), dtype=np.uint16)
    ts = np.zeros(len(events), dtype=np.uint64)
    p = np.zeros(len(events), dtype=np.uint8)
    i = 0
    for m in events:
        x[i] = m['x']
        y[i] = m['y']
        ts[i] = m['ts']['nsecs']
        p[i] = 1 if m['polarity'] else 0
        i += 1
    x_fin = np.array(np.concatenate([x_fin, x]), dtype=np.uint16)
    y_fin = np.array(np.concatenate([y_fin, y]), dtype=np.uint16)
    ts_fin = np.array(np.concatenate([ts_fin, ts]), dtype=np.uint64)
    p_fin = np.array(np.concatenate([p_fin, p]), dtype=np.uint8)
bag.close()
np.save("x.npy", x_fin)
np.save("y.npy", y_fin)
np.save("p.npy", p_fin)
np.save("ts.npy", ts_fin)