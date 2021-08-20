import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI Practice ++")
root.geometry("640x480")

def create_new_file():
    print("create new file..")
# 메뉴 생성
menu = Menu(root) 

# Edit 메뉴
menu.add_cascade(label="Edit") #화면에 보이는 부분 Edit - 기능은 현재 없음

# File 메뉴
menu_file = Menu(menu, tearoff=0) #tearoff = 점선이 표시되는 것을 방지
menu_file.add_command(label="New File", command=create_new_file) #클릭시 실행
menu_file.add_command(label="New Window") #이름표만
menu_file.add_separator() #구분 선 추가
menu_file.add_command(label="Open File") #이름표만
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비 활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) 
menu.add_cascade(label="File", menu=menu_file) # 화면에 보이는 부분 File 추가





# Language 메뉴
menu_lang = Menu(menu, tearoff=0) #언어 창 추가
menu_lang.add_radiobutton(label="Python") #체크하는 메뉴 3개
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)


# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap") #체크표시 유무 변경 가능
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()