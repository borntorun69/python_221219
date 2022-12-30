# Iterable은 차례로 요소를 접근할 수 있는 객체
# Iterator는 객체에 접근하기 위한 객체,원본영향 없음
# Iterator는 접근 순서유무에 상관없이 객체에 접근가능

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

s = set([1, 2, 3])
sitr = iter(s)  # set s에 접근하기 위한 iterator 생성
for item in sitr:
  print(item)
sitr = iter(s)
i = 1
while i < len(s):
  print(next(sitr), end='')
  i += 1
  print()

# 1)  반복문을 이영한 접근
i = 0
for item in a:
  print(f'{i}:{item}')
  i += 1

# 2) range를 이용한 접근
for i in range(len(a)):
  print(f'{i}: {a[i]}')

# 3) enumerate를 이용한 접근
for i, item in enumerate(a):
  print(f'{i}: {item}')

a.reverse()
print(a)
# 4) iterator를 이용한 접근
itr = reversed(a)  # iterator 타입으로 변환
print(itr)  # list reverseiterator만 출력
print(list(itr))
# print('iterator len:',len(a)) #error
# while item if next(a) else '':
#       print(item)
# list reverseiterator 한번쓰면 다시 초기화
print("==" * 20)
itr = reversed(a)  # iterator 한번쓰면 다시초기화
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

itr = iter(a)  # iterator 한번쓰면 다시초기화
for i in itr:
  print(i, end='')
print()
itr = iter(a)  # iterator 한번쓰면 다시초기화
i = 0
while i < len(a):
  print(next(itr), end='');
  i += 1
print()

