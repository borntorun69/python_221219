print(f'{" 형변환 함수 ":=^20}')
# 형 변환 함수
print(int("52"))
print(str(3.141592))

# print(int("3.141592")) #ValueError
print(float("3.145192"))
print(int(3.141592))  # 절삭
print(int(3.6))  # 절삭
print("==" * 20)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
for item in a:
  print(f'{i}:{item}')
  i += 1
for i in range(len(a)):
  print(f'{i}: {a[i]}')
for i, item in enumerate(a):
  print(f'{i}: {item}')

a = [1,2,3]
print(sum(a))
print(max(a))
print(min(a))

a.reverse()
print(a)
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

print("==" * 20)
print(f'{" math 함수 ":=^20}')
import math

print(math.ceil(3.141592))  # 절상
print(math.ceil(-3.141592))  # 절상

print(math.floor(3.741592))  # 절삭
print(math.floor(-3.741592))  # 절삭

# 문자열일때 홀수 짝수 구분
num = '30'
print('짝수' if num[-1] in '02468' else '홀수')

# 숫자일때 홀수 짝수 구분
num = 30
print('짝수' if num % 2 == 0 else '홀수')

print(f'{" Date 날짜/시간 관련 ":=^20}')
# import datetime
import datetime as dt

now = dt.datetime.now()
print("{}년 {}월".format((now.year), (now.month), (now.day)))
print("{}월".format(now.month))
print("{}일".format(now.day))
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

print("{}년 {}월 {}일".format(now.year, now.month, now.day))
print(now.strftime(("%Y-%m-%d %p %H:%M:%S:%A")))
# %H 24시, %I 12시간,%B 영어 월 %h 영어월짧게
# %a 영어요일 짧게, %p am/pm
print("월화수목금토일"[now.weekday()],
      "월월화수목금토일"[now.isoweekday()])

from datetime import date

d = date.fromordinal(730920)
print(d)
d1 = dt.date(2022, 12, 25)  # 임의 날짜 지정
print(d1.isoweekday())
