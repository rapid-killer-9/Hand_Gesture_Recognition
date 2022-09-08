import cv2
import numpy as np
import time
import math
import HandDetectionModule as hdm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


######################
wCam, hCam = 780, 720
######################


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
volBar = 400
area = 0


while True:
    SUCCESS, img = cap.read()
    detector.findHands(img,draw=True)
    lmList, bbox= detector.findPosition(img, drawPoints=True,drawBbox=True,points=[4,8])
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        area = (bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        if 250 < area < 700:
            print("Yes")
            
            length ,_,lineInfo= detector.findDistance(4,8,img,True)

            # Hand Range 50 to 190
            # Vol Range -95.25 to  0.0
            x, y = 50, 170
            vol = np.interp(length, [x, y], [minVol, maxVol])
            volBar = np.interp(length, [x, y], [400, 150])
            volPer = np.interp(length, [x, y], [0, 100])
            # print(int(length), vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < x:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 0, 255), cv2.FILLED)
            if length > y:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)}%', (45, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)

