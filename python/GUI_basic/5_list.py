from tkinter import *

root = Tk()
root.title("Hojun GUI") # 타이틀

root.geometry("640x480+400+100")

listbox = Listbox(root, selectmode="extended",height =0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END, "수박")
listbox.insert(END,"포도")
listbox.pack()



def btncmd():
    listbox.delete(0,END) # 맨 뒤에 항목을 삭제

    # 개수 확인 list.size()
    print("리스트에는",listbox.size(),"개가 있어요")

    # 항목 확인 - listbox.get()
    print("1번째부터 3번째까지의 항목: ",listbox.get(0,2))

    # 선택된 항목 확인
    print("선택된 항목은 : ",listbox.curselection())

    a = listbox.get(0)
    




btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
