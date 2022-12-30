# import my_util
# my_util.linez()

# import my_util as util
# util.linez()

from my_util import *
linez("재귀함수")

# 재귀함수 Recursive Call
# n! = n *(n-1)*(n-2)*(n-3)
# 3! = 3*2*1 = 1*2*3

# factorial를 for문으로 구현
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def factr(n):
  if n == 1:
    return 1
  else:
    return n * factr(n - 1)

print(factorial(5))
print(factr(5))

linez("콜백 함수")
def call_10_times(arg):
  for i in range(5):
    arg()

def my_hello():
  print('hello')

call_10_times(my_hello)

def power(item):
  return item * item

def under_3(item):
  return item < 3

l1 = [1,2,3,4,5]
print(l1)
l2 = map(power,l1)
print(list(l2)) #l2는 map object라서 바로 출력 안됨

l3 = filter(under_3, l1)
print(list(l3))

linez("람다(lambda)")

power = lambda x: x*x
under_3 = lambda x: x < 3

l1 = [1,2,3,4,5]
print(l1)
l2 = map(power,l1)
print(list(l2)) #l2는 map object라서 바로 출력 안됨

l3 = filter(under_3, l1)
print(list(l3))

# 람다의 인라인 방식
l2 = map(lambda x: x*x, l1)
l3 = filter(lambda x: x < 3, l1)

