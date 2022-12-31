import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from student_management.util import ui_util as tool
from tkinter import *
from tkinter import messagebox

dao = StudentDao() #생성자로 초기화 안하면 메서드 사용못함.

join = Tk()
join.title("Student Regist")
join.resizable(False, False)
tool.center_win(join,280,250)

name, id, pw, repw = StringVar(), StringVar(), StringVar(), StringVar()

def check_join():
  if str(name.get()) == "":
    messagebox.showinfo("알림","이름을 확인해주세요")
    ent_name.focus()
    return
  if str(id.get()) == "":
    messagebox.showinfo("알림","ID를 확인해주세요")
    ent_id.focus()
    return

  if str(pw.get()) == "":
    messagebox.showinfo("알림","비밀번호를 확인해주세요")
    ent_pw.focus()
    return
  if str(repw.get()) == "":
    messagebox.showinfo("알림","비밀번호 확인을 확인해주세요")
    ent_repw.focus()
    return

  if str(pw.get()) != str(repw.get()):
    messagebox.showinfo("알림", "비밀번호가 맞지 않습니다.")
    ent_pw.setvar("");ent_repw.setvar("")
    ent_pw.focus()
    return


def cancel():
  pass

tkinter.Label(join, text="Student Join")\
  .grid(row=0, columnspan=2)

Label(join, text="이름 : ", anchor=W)\
  .grid(row=1, column=0, padx=10, pady=10)
Label(join, text="ID : ")\
  .grid(row=2, column=0, padx=10, pady=10)
Label(join, text="비밀번호 : ")\
  .grid(row=3, column=0, padx=10, pady=10)
Label(join, text="비밀번호 확인 : ")\
  .grid(row=4, column=0, padx=10, pady=10)

ent_name = Entry(join, textvariable=name)
ent_name.grid(row=1, column=1, padx=10, pady=10)

ent_id = Entry(join, textvariable=id)
ent_id.grid(row=2, column=1, padx=10, pady=10)

ent_pw = Entry(join, textvariable=pw, show="*")
ent_pw.grid(row=3, column=1, padx=10, pady=10)

ent_repw = Entry(join, textvariable=repw, show="*")
ent_repw.grid(row=4, column=1, padx=10, pady=10)

Button(join, text="등록", width=10, command=check_join)\
  .grid(row=5, column=0, padx=10, pady=10, sticky=E)
Button(join, text="취소", width=10, command=cancel)\
  .grid(row=5, column=1, padx=10, pady=10, sticky='')

ent_name.focus()
join.mainloop()



