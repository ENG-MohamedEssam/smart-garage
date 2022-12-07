# Created by bassam at 10/14/2021

import cv2
import easyocr
import datetime
#############################################

frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
reader = easyocr.Reader(['en'], gpu=False)
minArea = 200
color = (255, 0, 255)
###############################################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
database={}
minute=0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            text = reader.readtext(imgRoi)
            text = text[0][1]
            if text not in database:
                minute = datetime.datetime.now().minute
                database[text]=minute
                count += 1
                print(database)
                cv2.waitKey(200)
            elif text in database:
                TotalTime = datetime.datetime.now().minute -database[text]
                print(TotalTime,"EL")
                database.pop(text)
                count -=1
                print(database)
                cv2.waitKey(200)

            cv2.imshow("ROI", imgRoi)

            cv2.putText(img, "Scan Saved", (70,50 ), cv2.FONT_HERSHEY_DUPLEX,
                        2, (0, 0, 255), 2)


            print(count, text, minute)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
