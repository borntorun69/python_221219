# while

a = list(range(1, 10))
i = 0
while i < len(a):
  if a[i] % 2 == 0: print(a[i])
  i += 1

while a:
  tmp = a.pop()
  if not tmp % 2: print(tmp)

# for item in a:
#   if item % 2 == 0:
#     print(item)

# break 활용
# i = 0
# while a:
#   if a[i] % 2 == 0:
#     print(a[i])
#   if (i < len(a)-1):  i += 1
#   else: break
import random

randNum = random.randrange(1, 101)
print(randNum)

# do while문 구현 ::  아래처럼 하면 실행이 2번
# 실행문
# while condition:
# 실행문

# do while문 구현 :: 아래는 조건이 반대
# while True:
#   실행문
#   if not condition: break

# 3) do while문 구현 :: 그나마 괜찮은 구문
# while True:
#    실행문
#    if not condition: break
#    break

# 3번으로 구현
cnt = 0
while True:
  ans = int(input('숫자 입력: '))
  cnt += 1
  if (ans > randNum):
    print('큽니다')
  elif (ans < randNum):
    print('작습니다')
  else:
    print("정답입니다. {}번만에 맞췄습니다".format(cnt))
    print(f"정답입니다. {cnt}번만에 맞췃습니다")
    break;
