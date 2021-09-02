from tkinter import *

root = Tk()
root.title("GUI Practice ++")
root.geometry("640x480")


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1, 32): # 1 ~ 31일
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

#listbox의 상하 움직임 매핑
scrollbar.config(command=listbox.yview)

root.mainloop()