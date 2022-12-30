# mod1.py
def add(a, b):
  print("__name__:",__name__)
  return a + b


def sub(a, b):
  return a - b

# __name__ 내장된 변수 이름

if __name__ == "__main__":
  print(add(1, 4))
  print(add(4, 2))


#파이썬에는 기본적으로 상수가 없다.
PI = 3.14
GRAVITY = 9.8

PI = 3.141592