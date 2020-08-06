import pickle
import time
import cv2
import mss
import numpy

BUFFER_SIZE = 4096


import socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

print('Sock name: {}'.format(sock.getsockname()))

while True:
    conn, addr = sock.accept()
    print('Connected:', addr)

    all_data = bytearray()

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        all_data += data

    obj = pickle.loads(all_data)
    print('Obj:', obj)

    print('Close')
    conn.close()
    break
cv2.imwrite('img.png', obj)
#cv2.imshow('image', obj)