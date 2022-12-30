from tkinter import *
from tkinter import ttk
from tkinter import messagebox

join = Tk()
join.title("Student Re")
name, id  = StringVar(), StringVar()
pw, repw = StringVar(), StringVar()

def check_join():
  if str(name.get()) == "":
    messagebox.showinfo("알림", "이름를 확인해주세요")
    entry1 = ttk.Entry(ent_name)
def check_join():
  if str(id.get()) == "":
    messagebox.showinfo("알림", "ID를 확인해주세요")
    entry1 = ttk.Entry(ent_id)
def check_join():
  if str(pw.get()) == "":
    messagebox.showinfo("알림", "비밀번호를 확인해주세요")
    entry1 = ttk.Entry(ent_pw)
def check_join():
  if str(repw.get()) == "":
    messagebox.showinfo("알림", "비밀번호를 재확인해주세요")
    entry1 = ttk.Entry(ent_repw)


def go_login():
  pass

#==========================================
ttk.Label(join, text="이 름 : ") \
  .grid(row=0, column=0, padx=10, pady=10)
ttk.Label(join, text="ID : ") \
  .grid(row=1, column=0, padx=10, pady=10)
ttk.Label(join, text="비밀번호 : ") \
  .grid(row=2, column=0, padx=10, pady=10)
ttk.Label(join, text="비밀번호재확인 : ") \
  .grid(row=3, column=0, padx=10, pady=10)

#===========================================
ent_name = ttk.Entry(join, textvariable=name)
ent_name.grid(row=0, column=1, padx=10, pady=10)

ent_id = ttk.Entry(join, textvariable=id)
ent_id.grid(row=1, column=1, padx=10, pady=10)

ent_pw = ttk.Entry(join, textvariable=pw, show="*")
ent_pw.grid(row=2, column=1, padx=10, pady=10)

ent_repw = ttk.Entry(join, textvariable=repw, show="*")
ent_repw.grid(row=3, column=1, padx=10, pady=10)
entry1 = ttk.Entry(ent_name)

#============================================
ttk.Button(join, text="등록", command=check_join) \
  .grid(row=4, column=0, padx=10, pady=10)

ttk.Button(join, text="취소", command = go_login) \
  .grid(row=4, column=2, padx=10, pady=10)

join.mainloop()