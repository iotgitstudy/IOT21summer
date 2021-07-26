from tkinter import *

root = Tk()
root.title("Hojun GUI") # 타이틀
root.geometry("640x480+400+100")


txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요.")


e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력하시요")


def btncmd():
    print(txt.get("1.0",END)) # 첫번째 라인에서 0번째 컬럼위치, # 내용 추출
    print(e.get())

    txt.delete("1.0",END)  # 내용 삭제
    e.delete(0,END)

btn =Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()