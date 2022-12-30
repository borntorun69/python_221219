import time, threading, requests, random, sys
import tkinter as tk
from tkinter import simpledialog


class Bomb(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.life = random.randint(1, 2)
    self.state = False

  def run(self):
    for i in range(10, 0, -1):
      if self.state: break
      print(i)
      time.sleep(0.3)
    print("Bomb~~~!")
    sys.exit()

  def choose(self, line):
    try:
      line = int(line)
    except Exception as e:
      line = ()
    print(f'{line}을 선택하셨습니다.')
    if (self.life == line):
      print("살았습니다")
    else:
      print("으악 ~~!")
    self.state = True


# b = bomb.Bomb
# b.start()
# print(b.life)
#
# appLication_window = tk.Tk()
# answer = simpledialog.askstring(
#   "Select", "Which do you want red(1) or blue(2)?",
#   parent=None)
# b.choose(answer)
