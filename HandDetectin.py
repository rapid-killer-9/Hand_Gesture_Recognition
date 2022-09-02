import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
CTime = 0


while True:
    SUCCESS, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for ind, ln in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(ln.x*w), int(ln.y*h)
                if id == 4 or id == 8:
                    print(id, cx, cy)
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), 2)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (57, 255, 20), 2)
           
    cv2.imshow("Image", img)
    cv2.waitKey(1)
