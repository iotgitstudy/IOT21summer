import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)

keys = [['Q', 'W', 'E','R','T','Y','U','I','O','P','[',']'],
       ['A','S','D','F','G','H','J','K','L',';',"'"],
       ['Z','X','C','V','B','N','M',',','.','/'] ]
def drawALL(img, buttonList):
    for button in buttonList:

        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x+w, y+h), (255, 0,255), cv2.FILLED)
        cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN,
        4, (255, 255, 255), 4)

    return img

class Button():
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text


        


buttonList = []
for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100*j+50, 100*(i+1)+50], key))


    
while True:
    
    success, img = cap.read()
    img = cv2.flip(img, 1) #화면 좌우 반전

    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    
    img = drawALL(img, buttonList)
    


    cv2.imshow("image", img)
    exit = cv2.waitKey(1)


    #종료버튼 : q
    if exit ==ord("q"): 
        break