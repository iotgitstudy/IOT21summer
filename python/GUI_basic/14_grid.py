from tkinter import *

root = Tk()
root.title("GUI Practice ++")
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

#pack은 쌓는 느낌

#btn1.pack()
#btn2.pack()

#btn1.pack(side="left")
#btn2.pack(side="right")


#btn1.grid(row=0, column=0)
#btn2.grid(row=1, column=1)

# 맨 윗줄

btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

#clear 줄
btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)

# 7 시작 줄
btn_7 = Button(root, text="7")
btn_8 = Button(root, text="8")
btn_9 = Button(root, text="9")
btn_sub = Button(root, text="-")

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

# 4 시작 줄
btn_4 = Button(root, text="4")
btn_5 = Button(root, text="5")
btn_6 = Button(root, text="6")
btn_add = Button(root, text="+")

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

# 1시작 줄

btn_1 = Button(root, text="4")
btn_2 = Button(root, text="5")
btn_3 = Button(root, text="6")
btn_enter = Button(root, text="enter") #세로로 합쳐짐

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_enter.grid(row=4, column=3, rowspan=2)

# 0 시작 줄

btn_0 = Button(root, text="0") #가로로 합쳐짐
btn_point = Button(root, text=".")

btn_0.grid(row=5, column=0, columnspan=2)
btn_point.grid(row=5, column=2)


root.mainloop()
