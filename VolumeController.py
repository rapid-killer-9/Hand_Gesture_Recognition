import cv2
import numpy as np
import time
import math
import HandDetectionModule as hdm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import streamlit as st


######################
wCam, hCam = 748, 580
######################

st.title("Hand Gesture")

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

cTime, pTime = 0, 0

detector = hdm.HandDetector(detectionCon=0.7)




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()


minVol = volRange[0]
maxVol = volRange[1]


while True:
    SUCCESS, img = cap.read()
    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 10, (0, 0, 255), 2)
        cv2.circle(img, (x2, y2), 10, (0, 0, 255), 2)
        # cv2.circle(img, (cx, cy), 7, (0, 0, 255), 2)

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        length = math.hypot(x2-x1, y2-y1)

        # Hand Range 50 to 190
        # Vol Range -95.25 to  0.0
        x, y = 50, 170
        vol = np.interp(length, [x, y], [minVol, maxVol])
        volBar = np.interp(length, [x, y], [400, 150])
        volPer = np.interp(length, [x, y], [0, 100])
        # print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < x:
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        if length > y:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)}%', (45, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)

