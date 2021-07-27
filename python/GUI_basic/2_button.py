#GUI 라이브러리 import
from tkinter import *

#tkinter 선언
root = Tk()

root.title("IOT GUI") #제목


##########버튼 예제
btn1 = Button(root, text="버튼1")
btn1.pack()

#padx padt :여백 - 글자수에 따라 더 커질 수 있음
btn2 = Button(root, padx=5, pady=10, text="버튼222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

#width, height : 고정 크기
btn4 = Button(root, width=10, height=3, text="버튼44444444444")
btn4.pack()
#fg = 글자 색, bg= 배경 색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="python/GUI_basic/btn.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼 클릭됨")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()
#창이 닫히지 않도록 유지
root.mainloop()