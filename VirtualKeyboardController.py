import cv2
import HandDetectionModule as hdm

cap = cv2.VideoCapture(0)
cap.set(3, 780)
cap.set(4, 720)

detector = hdm.HandDetector(detectionCon=0.8)
while True:
    success, img = cap.read()
    img = detector.findHands(img)

    lmList = detector.findPosition(img)
    bboxInfo = detector.findPosition(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
