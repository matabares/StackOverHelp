import socket
import time
import cv2
import mss
import numpy
with mss.mss() as sct:
    monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 640}

    for _ in range(1):
        obj = numpy.array(sct.grab(monitor))
        obj = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Send:', obj)

import pickle
data = pickle.dumps(obj)

sock.sendall(data)

print('Close')
sock.close()