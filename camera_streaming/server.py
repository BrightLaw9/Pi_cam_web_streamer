import socket, cv2, pickle, base64, struct

HOST = "127.0.0.1"
PORT = 8000

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
            frame = cv2.resize(frame, (320, 320))
            #frame = cv2.imread("/Users/lawre/BrickPi_web_cam_streamer/camera_streaming/IMG-7988.jpg")
            serialized = pickle.dumps(frame)
            message = struct.pack("Q", len(serialized))+serialized
            #retval, buffer = cv2.imencode('.jpg', frame)
            #imgBytes = base64.b64encode(buffer)
            #imgStr = imgBytes.decode('ascii')
            #json_object = json.dumps({'img_str':imgStr})
            #Send img data
            conn.sendall(message) 
            
