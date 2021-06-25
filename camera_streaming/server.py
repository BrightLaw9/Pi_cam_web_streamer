import socket
import cv2

HOST =
PORT = 

cap = cv2.VideoCapture(0)

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Established connection with: ", addr)
        while True:
            #Capture img using camera
            ret, frame = cap.read()
            #Send img data
            conn.sendall(frame) 
            
