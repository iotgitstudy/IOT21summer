##주의사항 - 파일 디렉터리 경로 잘 파악하기 강의 내용과 GUI가 다르고 경로도 다름

#GUI 라이브러리 import
from tkinter import *

#tkinter 선언
root = Tk()
root.geometry("640x480+100+200") #가로 * 세로 + x좌표 + y좌표
root.title("IOT GUI") #제목

#label = 그냥 텍스트 표시 됨
label1 = Label(root, text="안녕하세요")
label1.pack()

#그냥 이미지만 띄움 기능 X
photo = PhotoImage(file="GUI_basic/btn.png")
label2 = Label(root, image=photo)
label2.pack()

#레이블 변경 기능 함수
def change():
    #기존 레이블 텍스트 변경
    label1.config(text="또 만나요")
    global photo2 #전역변수 선언

    #2번째 이미지 선언
    photo2 = PhotoImage(file="GUI_basic/img2.png")
    #이미지 변경
    label2.config(image=photo2)

#command인자로 버튼에 기능 추가
btn = Button(root, text="클릭", command=change)
btn.pack()

#창이 닫히지 않도록 유지
root.mainloop()