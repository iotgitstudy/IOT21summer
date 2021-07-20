#GUI 라이브러리 import
from tkinter import *

#tkinter 선언
root = Tk()

root.title("IOT GUI") #제목

#root.geometry("640x480") #가로 * 세로

root.geometry("640x480+100+200") #가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 고정

#창이 닫히지 않도록 유지
root.mainloop()