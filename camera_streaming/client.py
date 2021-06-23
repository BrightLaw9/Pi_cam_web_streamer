import socket
import cv2

HOST =
PORT =


with socket.socket() as s:
    s.connect((HOST, PORT))
    while True:
        #Get img data from server 
        img = s.recv(2048) # <-- Number of bytes receive from client device

        cv2.imshow('frame', img) 
