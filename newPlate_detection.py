import cv2
import easyocr
import datetime
import serial
import time
#############################################
arduino = serial.Serial(port ='COM6', baudrate = 9600, timeout = 0.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


# arduino = serial.Serial(port ='COM6', baudrate = 9600, timeout = 0.1)
time.sleep(1)
reader = easyocr.Reader(['en'], gpu=True)
cap = cv2.VideoCapture(1)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 100)
count = 0

# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data

while True:
    success, img = cap.read()

    text = reader.readtext(img)
    if len(text)>0:
        out=[]
        for i in range(len(text)):
            text1 = text[i][1]
            out.append(text1)
            write_read(str(text1))
            cv2.waitKey(500)
        print(len(text))
        write_read('8')
        #cv2.waitKey(1000)

        print(out)
        # print(len(text))
        # text1 = text[0][1]
        # print(text1)
        # text1 = text[1][1]
        # print(text1)
        # length=len(text)
        #
        # print(text)

       # num = text
        # value = write_read(num)
        # print(value)
    elif len(text) == 0:
        write_read('9')
        print("hi iam here")


    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
