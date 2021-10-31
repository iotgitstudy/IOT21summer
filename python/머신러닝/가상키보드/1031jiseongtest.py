import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)

class Button():
    def __init__(self, pos, text, size=[100,100]):
        self.pos = pos
        self.size = size
        self.text = text
        cv2.rectangle(img, self.pos, self.size, (255, 0,255), cv2.FILLED)
        cv2.putText(img, self.text, (self.pos[0]+25, self.pos[1]+25), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)





while True:
    
    success, img = cap.read()
    img = cv2.flip(img, 1) #화면 좌우 반전

    
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    
    mybutton = Button([100,100], "Q")

    cv2.imshow("image", img)
    exit = cv2.waitKey(1)


    #종료버튼 : q
    if exit ==ord("q"): 
        break