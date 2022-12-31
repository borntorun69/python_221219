from tkinter import *
from tkinter import messagebox
from student_management.util import ui_util as tool
from student_management.dao.dao_student import StudentDao
from student_management.vo.student_vo import Student

login = Tk()
id, pw = StringVar(), StringVar()
dao = StudentDao()

def check_login():
  if str(id.get()) == "":
    messagebox.showinfo("알림","ID를 확인해주세요")
    ent_id.focus()
    return

  if str(pw.get()) == "":
    messagebox.showinfo("알림","비밀번호를 확인해주세요")
    ent_pw.focus()
    return
  s = Student()
  s.id = id.get()
  s.pw = pw.get()
  result = dao.login_check(s)
  print(result)

def go_join():
  pass

Label(login, text="ID : ")\
  .grid(row=0, column=0, padx=10, pady=10)
Label(login, text="Password : ")\
  .grid(row=1, column=0, padx=10, pady=10)

ent_id = Entry(login, textvariable=id)
ent_id.grid(row=0, column=1, padx=10, pady=10)

ent_pw = Entry(login, textvariable=pw, show="*")
ent_pw.grid(row=1, column=1, padx=10, pady=10)

Button(login, text="Login", width=10, command=check_login)\
  .grid(row=2, column=0, padx=10, pady=10, sticky='e')
Button(login, text="Join", width=10, command=go_join)\
  .grid(row=2, column=1, padx=10, pady=10, sticky='')

ent_id.focus()
tool.center_win(login,270,150)
login.mainloop()
