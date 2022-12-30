# if 조건:
#   실행문 ...

# if 조건:
#   실행문
# elif 조건:
#   실행문
# elif 조건:
#   실행문
# elif 조건:
#   실행문
# else 조건:
#   실행문

# score = \
#   int(input("접수 입력(0은 종료)"))
score = 99
result = ''
if score >= 90:
  result = 'A'
elif score >= 80:
  result = 'B'
elif score >= 70:
  result = 'C'
elif score >= 60:
  result = 'D'
else:
  result = 'F'
print('학점:', result)

a = 1
if a in (1, 2, 3,) and a != 0:
  pass # 나중애 정의 하려고 지금은 패스
  # print('포함')
  # raise NotImplementedError
else:
  print('부재')

print('포함' if a not in [1, 2, 3] else '부재') #list
print('포함' if a not in (1, 2, 3) else '부재') #tuple
print('포함' if 'money' in ["show","me",'the',"money"] else '부재') #문자열 리스트

message = "포함" if a in [1,2,3] else '부재'

