import bomb
import tkinter as tk
from tkinter import simpledialog

b = bomb.Bomb()
b.start()
print(b.life)

appLication_window = tk.Tk()
answer = simpledialog.askstring(
  "Select", "Which do you want red(1) or blue(2)?",
  parent=None)
b.choose(answer)
