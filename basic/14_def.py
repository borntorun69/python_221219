# 함수 기능들의 묶음
from typing import Iterable


def lines():
  print("==" * 12)


def linez(str):
  print(f'{" " + str + " ":=^20}')


def printIterable(obj):
  # if hasattr(obj, "__iter__"):
  if isinstance(obj, Iterable):
    for item in obj:
      print(f'{item}', end='')
    print()
  else:
    print(obj)


a = [1, 2, 3, 4, 5]
printIterable(a)
printIterable('hello world')
printIterable(123)
print(printIterable(111))  # None 출력
lines()


def add(a, b):
  return a + b


add(1, 1)
print(add(1, 1))  # return 있기 때문에
lines()
# 매개변수 갯수가 맞지 않으면 TypeError 발생
# print(add(1, 2, 3))

linez("가변 매개변수")


def add(n, *values):
  for i in range(n):
    for val in values:
      print(val, end=' ')
    print()


add(3, 1, 2, 3, 4, 5)


def sums(*values):
  for val in values:
    print(val, end=' ')
  print()


sums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

linez("기본 매개변수")


# 기본 매개변수는 맨 뒤에 놓을 것

def defaultPrint(n1=10, n2=10):
  return n1 * n2


print(defaultPrint(10))

linez("매개변수 지정하여 호출")


# 기본 매개변수는 맨뒤에 놓을것

def defaultPrint(n1=10, n2=10):
  return n1 - n2


print(defaultPrint(n2=2, n1=1))

linez("응용1) 다양한 매개변수 호출")


def test(a, b=10, c=20):
  print(a + b + c)


test(1, 2, 3)  # 기본 대입형태
test(a=1, b=2, c=3)  # 매개변수 지정형태
test(10, c=20)

linez("응용2) 자료없이 리턴")


def test_condition(sw):
  if (sw):
    print('a')
    return "a"  # 리턴이 있을 때 : 오직 하나
  else:
    return  # 리턴이 없을 때 : 함수의 진행끝
  print('b')


print(test_condition(1))

linez("응용3) 매개변수와 리턴 응용")


def sum_all(start=0, end=100, step=1):
  output = 0
  for i in range(start, end + 1, step):
    output += i
  return output


print("1", sum_all(0, 100, 10))
print("2", sum_all(end=100))
print("3", sum_all(end=100, step=2))

linez("매개변수의 Scope")
# 함수 네부의 변수는 할당이 되면 지역변수이다.
a = 1
def vartest(a):
  a = a + 1
  return a

vartest(a)
print(a)
a = vartest(a)
print(a)  # 함범위 밖의 변수에도 영향

def vartest2():
  global a  # 외부에 선언된 변수를 사용할 때
  # 함수 내부에서 외부에 선언된 변수는 참조만 가능
  # 함수 내부에서 같은 이름으로 선언 하면 연산까지 가능
  # 함수 내부의 global함수는 내 외에서 사용가능
  # 함수 내부에만 선언된 global 변수는 함수실행후 외부에서 사용가능
  a += 1
  return a


vartest2()
print(a)

def vartest(b):
  b = b + 1
  return b

vartest(3)
# print(b) #NameError: name 'b' is not defined

linez("global")
num = 100
def add2():
  global numaa
  # 함수 내부에서 외부에 선언된 변수는 참조만 가능
  # 함수 내부에서 같은 이름으로 선언 하면 연산까지 가능
  # 함수 내부의 global함수는 내 외에서 사용가능
  # 함수 내부에만 선언된 global 변수는 함수실행후 외부에서 사용가능
  # b = num + 100
  num = 0
  num += 100
  numaa = 100
  print(numaa)

add2()
print(numaa)
# add2()
#
print(numaa)




