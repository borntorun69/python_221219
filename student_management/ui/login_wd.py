# import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from student_management.util import ui_util as tool
from student_management.dao.dao_student import StudentDao
from student_management.vo.student_vo import Student


login = Tk()
id,pw = StringVar(), StringVar()
dao = StudentDao()


def check_data():
  if ent_id.get() == "Passing" and ent_pw.get() == "Story":
    # 새로운 화면 생성
    newwin = Tk()
    Tk.Label(newwin, text="Welcome to " + ent_id.get()).grid(row=0, column=0, padx=10, pady=10)
    newwin.mainloop()
    print("Logged IN Successfully")
  else:
    print("Check your Username/Password")
def check_login():
  if str(id.get()) == "":
    messagebox.showinfo("알림","ID를 확인해주세요")
    ent_id.focus()
    # entry1 = ttk.Entry(ent_id)
    # ent_id.focus_force()
    # ent_id.pack()
  if str(pw.get()) == "":

def go_join():
  pass

ttk.Label(login, text="ID : ")\
  .grid(row=0,column=0,padx=10, pady=10)
ttk.Label(login, text="Password : ")\
  .grid(row=1,column=0,padx=10, pady=10)

ent_id = ttk.Entry(login, textvariable=id)
ent_id.grid(row=0,column=1,padx=10, pady=10)

ent_pw = ttk.Entry(login, textvariable=pw, show="*")
ent_pw.grid(row=1,column=1,padx=10, pady=10)
# entry1 = ttk.Entry(ent_id)
# entry1.focus_displayof()



Button(login, text="Login", command=check_login)\
  .grid(row=2,column=0,padx=10, pady=10)
Button(login, text="Join", command=go_join)\
  .grid(row=2,column=2,padx=10, pady=10)

ent_id.focus()
tool.center_win(login,270,150)
login.mainloop()
