import cv2
import HandDetectionModule as hdm
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = hdm.HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 15, y + 55),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

class Button():
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.size = size
        self.text = text



buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([90 * j + 50, 90 * i + 50], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw = True)
    lmList,bboxInfo = detector.findPosition(img,drawPoints=True,drawBbox=True,points=[8])
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x , y = button.pos
            w , h = button.size

            if (x< lmList[8][1]< x+w) and (y< lmList[8][2]< y+h):
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255 , 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 60),cv2.FONT_HERSHEY_PLAIN , 4, (255, 255, 255), 4)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
