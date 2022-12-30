from tkinter import *
from tkinter import ttk

login = Tk()
id,pw = StringVar(),""

def check_login():
  pass
def go_join():
  pass

ttk.Label(login, text="ID : ")\
  .grid(row=0,column=0,padx=10, pady=10)
ttk.Label(login, text="Password : ")\
  .grid(row=1,column=0,padx=10, pady=10)

ttk.Entry(login, textvariable=id)\
  .grid(row=0,column=1,padx=10, pady=10)
ttk.Entry(login, textvariable=pw, show="*")\
  .grid(row=1,column=1,padx=10, pady=10)

ttk.Button(login, text="Login", command=check_login)\
  .grid(row=2,column=0,padx=10, pady=10)
ttk.Button(login, text="Join", command=go_join)\
  .grid(row=2,column=2,padx=10, pady=10)

login.mainloop()