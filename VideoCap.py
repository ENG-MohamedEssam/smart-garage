import cv2

cap = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin&password=alex1234&channel=4&stream=0.sdp?real_stream--rtp-caching=100")
#cap2 = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin&password=alex1234&channel=1&stream=0.sdp?real_stream--rtp-caching=100")

while True:
    success, img = cap.read()
    #success, img2 = cap2.read()
    cv2.imshow("Cam1", img)
    #cv2.imshow("Cam2", img2)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break