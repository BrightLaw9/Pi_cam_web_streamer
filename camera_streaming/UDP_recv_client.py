import socket, cv2, pickle, base64
import numpy as np
import struct

HOST = "127.0.0.1"
PORT = 8000


with socket.socket(type=socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data = b''
    while True:
        payload = struct.calcsize("Q")
        #Get img data from server 
        #Possible GPU acceleration? 
        while len(data) < payload: 
            data += s.recvfrom(8192) # <-- Number of bytes receive from client device
        #img_str = json.loads(data)['img_str']
        #img_bytes = img_str.encode('ascii')
        #decoded_img = base64.b64decode(data)
        #np_frame = np.frombuffer(decoded_img, dtype=np.uint8)
        msg = data[:payload]
        data = data[payload:]
        msgSize = struct.unpack("Q", msg)[0]
        print("done1")

        while len(data) < msgSize:
            data += s.recvfrom(8192)
        frame_data = data[:msgSize]
        data = data[msgSize:]
        frame = pickle.loads(frame_data)
        cv2.imshow("R", frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
