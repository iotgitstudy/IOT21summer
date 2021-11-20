import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
import time

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8, maxHands=2)
finalText = ''
keys = [['Q', 'W', 'E','R','T','Y','U','I','O','P'],
       ['A','S','D','F','G','H','J','K','L'],
       ['Z','X','C','V','B','N','M'] ]

keyboard = Controller()

def drawALL(img, buttonList):
    for button in buttonList:

        x, y = button.pos
        w, h = button.size
        #cv2.rectangle(img, button.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x+5, y+45), cv2.FONT_HERSHEY_PLAIN,
        4, (255, 255, 255), 3)

    return img

class Button():
    def __init__(self, pos, text, size=[50,50]):
        self.pos = pos
        self.size = size
        self.text = text





buttonList = []
for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([50*j+300, 70*(i+1)+450], key))

flag = False
start = 1000000000000000000
xx = yy = ww = hh = 0
now_text = ''
while True:
    
    success, img = cap.read()
    img = cv2.flip(img, 1) #화면 좌우 반전

    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    
    img = drawALL(img, buttonList)
    
    if lmList: #손이 있는지 체크
        for button in buttonList:
            x, y = button.pos # 버튼 위치
            w, h = button.size # 버튼 크기


            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h: # 8번 인자 = 검지 손가락 끝이 버튼 범위 안에 있으면 
                cv2.rectangle(img, button.pos, (x+w, y+h), (0, 255, 0), cv2.FILLED) # 색 변경
                cv2.putText(img, button.text, (x+5, y+45), cv2.FONT_HERSHEY_PLAIN,
                4, (255, 255, 255), 3)

                xx, yy, ww, hh = x, y, w, h
                now_text = button.text
                #l, _, q_ = detector.findDistance(7, 8, img, draw=False) # 검지와 중지 사이의 거리 체크
                #print(l) 

                # 클릭 시
                #if l < 3:
                #    #keyboard.press(button.text)
                #    cv2.rectangle(img, button.pos, (x+w, y+h), (175, 0, 175), cv2.FILLED) # 색 변경
                #    cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN,
                #    4, (255, 255, 255), 4)
                #    finalText += button.text
                #    sleep(0.15)
            if xx < lmList[8][0] < xx + ww and yy < lmList[8][1] < yy + hh:
                if not flag:
                    start = time.time()
                    flag = True
                if time.time() - start > 0.6:
                    finalText += now_text
                    
                    start = time.time()
            else:
                start = time.time()
            print(time.time() - start)    

    #cv2.rectangle(img, (50,550), (700, 450), (175, 0, 175), cv2.FILLED) # 색 변경
    cv2.putText(img, finalText, (60, 525), cv2.FONT_HERSHEY_PLAIN,
    5, (255, 255, 255), 5)




    cv2.imshow("image", img)
    exit = cv2.waitKey(1)


    #종료버튼 : q
    if exit ==ord("q"): 
        break