#import
from tkinter import *
#기본 head
root = Tk()
root.title("GUI")


# 파일 프레임
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=12)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=12)
btn_del_file.pack(side="right")


# 리스트 프레임

list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # 높이 확장

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")




#화면 설정
root.resizable(False, False)
root.mainloop()