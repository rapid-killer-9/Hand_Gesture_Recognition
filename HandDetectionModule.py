import cv2
import mediapipe as mp
import time
import math


class HandDetector:
    def __init__(self, mode=False, maxHands=2, complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.complexity = complexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, drawPoints = True, drawBbox = True, points = [4]):
        self.lmList = []
        xList = []
        yList = []
        bbox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, ln in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(ln.x * w), int(ln.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if drawPoints:
                    for x in points:
                        if id == x:
                            cv2.circle(img, (cx, cy), 10, (0, 0, 255), 2)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
            if drawBbox:
                cv2.rectangle(img, (bbox[0]-20,bbox[1]-20), (bbox[2]+20,bbox[3]+20), color=(0, 255, 0),thickness=2)
        return self.lmList , bbox

    def fingerUp(self):
        finger = []
        #thumb
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)
        # 4 fingers
        for id in range(1,5):
            if self.lmList[self.tipids[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        return finger

    def findDistance(self, p1, p2, img,draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1],self.lmList[p2][2]

        cx, cy = (x1+x2)//2, (y1+y2)//2
        if draw:
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), 2)
            # cv2.circle(img, (cx, cy), 7, (0, 0, 255), 2)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        length = math.hypot(x2-x1, y2-y1)

        return length , img , [x1,x2,y1,y2,cx,cy]


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        SUCCESS, img = cap.read()
        img = detector.findHands(img)
        lmlist, bbox = detector.findPosition(img)
        # if len(lmlist) != 0:
        #     print(lmlist[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (57, 255, 20), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
