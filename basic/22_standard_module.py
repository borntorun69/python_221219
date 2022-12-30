from my_util import *
#파이썬에서 모듈(표준모듈,외부모듈)

#내장형 함수
print(abs(-10))
#all 모두 만족할때
print("all([1,2,3]):",all([1,2,3])) #all의 매개변수는 iterable
print("all([0,2,3]):",all([0,2,3])) #all의 매개변수는 iterable

#any 하나라도 만족할때
print("any([0,3,0]):",any([0,3,0]))
print("any([0,0,0]):",any([0,0,0]))

#chr 아스키코드값을 문자로
print(chr(97))

#dir 매개변수 타입에 따른 함수, 변수 리스트 보여줌
# print(dir([1,2,3]))
# print(dir({'key':'value'}))

# divmod
print("divmod(10,3):",divmod(10,3))
pr("divmod(10,3)")
# enumerate
for i, item in enumerate([1,2,3]):
  print(f'{i}:{item}')

#eval
print(eval('all([1,2,3])'))
pr("eval('all([1,2,3])')")

pr("hex(234)")
#1) 함수로 처리
def two_times(l):
  result = []
  for i in l:
    result.append(i*2)
  return  result
print(two_times([1,2,3,4]))

#2) 콜백함수 처라
def two_times(x):
  return x * 2

print(list(map(two_times,[1,2,3,4])))

#3) lamda 처리
print(list(map(lambda x: x*2,[1,2,3,4])))

print(max([1, 2, 3]))

# import tkinter as tk
# from tkinter import simpledialog
# application_window = tk.Tk()
# answer = simpledialog.askstring(
#   "Input","What is your first name?",
#   parent = None )
# print('answer:',answer)








# from tkinter import messagebox
# messagebox.showinfo("알림","정보")
# messagebox.showinfo("에러","문제")
# messagebox.showinfo("경고","조심")





# import ctypes
# ctypes.windll.user32.MessageBoxW(
#   0, "원하는 메시지를 입력하세요.","희망의 소리",16)



# import math
# print(math.sin(1))

