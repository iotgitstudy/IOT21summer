# 메모장 만들기

#######################

#GUI 라이브러리 import
from tkinter import *
import os
#tkinter 선언
root = Tk()

root.title("제목 없음 - Windows") #제목

#root.geometry("640x480") #가로 * 세로

root.geometry("640x480+100+200") #가로 * 세로 + x좌표 + y좌표
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = "mynote.txt"
def open_file():
    txt.delete("1.0",END)
    if os.path.isfile(filename):
        f = open(filename, "r")
        lines = f.readlines()
        for line in lines:
            txt.insert(END, line)

        
        f.close()

def save_file():
    if os.path.isfile(filename):
        f = open(filename, "w")
        lines = txt.get("1.0", END)
        f.write(lines)
        f.close()
def exit():
    root.destroy()


frame = Frame(root, bd=1)
frame.pack(fill="both", expand=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
menu = Menu(frame)

menu_파일 = Menu(menu, tearoff=0)

menu.add_cascade(label="파일(F)", menu=menu_파일) # 화면에 보이는 부분 File 추가
menu_파일.add_command(label="새로 만들기") 
menu_파일.add_command(label="새 창") 
menu_파일.add_command(label="열기", command=open_file) #클릭시 실행
menu_파일.add_command(label="저장", command=save_file) #클릭시 실행
menu_파일.add_command(label="다른 이름으로 저장") 
menu_파일.add_separator() #구분 선 추가
menu_파일.add_command(label="페이지 설정") 
menu_파일.add_command(label="인쇄") 
menu_파일.add_separator() #구분 선 추가
menu_파일.add_command(label="끝내기", command=exit) #클릭시 실행
menu_편집 = Menu(menu, tearoff=0)

menu.add_cascade(label="편집(E)", menu=menu_편집) # 화면에 보이는 부분 File 추가
menu_편집.add_command(label="실행 취소(U)             Ctrl+Z") 
menu_편집.add_separator() #구분 선 추가
menu_편집.add_command(label="잘라내기")
menu_편집.add_command(label="복사")
menu_편집.add_command(label="붙여넣기")
menu_편집.add_command(label="삭제")
menu_편집.add_separator() #구분 선 추가
menu_편집.add_command(label="Bing으로 검색")
menu_편집.add_command(label="찾기")
menu_편집.add_command(label="다음 찾기")
menu_편집.add_command(label="이전 찾기")
menu_편집.add_command(label="바꾸기")
menu_편집.add_command(label="이동")
menu_편집.add_separator() #구분 선 추가
menu_편집.add_command(label="모두 선택")
menu_편집.add_command(label="시간/날짜")


menu_서식 = Menu(menu, tearoff=0)
menu_서식.add_command(label="자동 줄 바꿈(W)")
menu_서식.add_command(label="글꼴(F)...")
menu.add_cascade(label="서식(O)", menu=menu_서식) # 화면에 보이는 부분 File 추가

menu_보기 = Menu(menu, tearoff=0)
menu_보기.add_command(label="확대하기/축소하기")
menu_보기.add_command(label="상태표시줄(S)")
menu.add_cascade(label="보기(V)", menu=menu_보기) # 화면에 보이는 부분 File 추가

menu_도움말 = Menu(menu, tearoff=0)
menu_도움말.add_command(label="도움말 보기(H)")
menu_도움말.add_command(label="피드백 보내기(F)")
menu_도움말.add_separator() #구분 선 추가
menu_도움말.add_command(label="메모장 정보(A)")

menu.add_cascade(label="도움말(H)", menu=menu_도움말) # 화면에 보이는 부분 File 추가



#쓰기 영역
txt = Text(frame,yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)

#창이 닫히지 않도록 유지
root.mainloop()