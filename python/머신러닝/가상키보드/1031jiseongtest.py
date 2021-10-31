import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector()

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    
    
    cv2.imshow("image", img)
    cv2.waitKey(1)