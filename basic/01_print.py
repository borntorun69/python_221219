# print()
print(52)
print(52, 273, "Hello Python")
print(10, 20, 30)
print("Hello", "My name is", "LGH")
print()  # 한줄 띄우기

print("# 특수문자(escape letter)")
print("# \\n \\t \\' \\\" ")
print('Hello', "Python", '"쌍따옴표"', "'홀따옴표'")
print("\"쌍따옴표\" \\ \'escape문자\'")
print("동해물과 백두산이 마르고 닮도록 \n"
      "하느님이 보우하사 우리나라 만세")
# 여러줄 문자열 """
print(
  """동해물과 백두산이 마르고 닮도록 
        "하느님이 보우하사 우리나라 만세""")
print()

# print()의 속성 ,end=
print(10, 20, end="끝 \n")
# import time
#
# for i in range(10):
#     print(i, end='')
#     time.sleep(1)
print()
print(10, 20, 30, 40, 50, sep="🙀")
with open('./hello.txt', "w") as f:
  print('Hello Python', file=f)
f = open('./hello.html', 'r')
lines = f.readlines()
for line in lines:
  print(line)
f.close()
# flush 스트랩을 강제할 것인지에 대한 여부(True, False)
print("# print처럼 사용하기")
print("number={0}, name={1}".format(1000, 'LGH'))
print("%d %s" % (1000, "LGH"), end='.\n')
print()

# 들여쓰기로 인한 공백을 없에기 위한 방법
if (2 > 1):
  print('첫번째 줄 \
        두번재 줄 \
        세번째 줄')
if (2 > 1):
  print('''첫번째 줄 
        두번재 줄 
        세번째 줄''')
if (2 > 1):
  print('''첫번째 줄\n두번재 줄\n세번째 줄''')

if (2 > 1):
  str = ("첫번째 줄 \n" '두번째 줄 \n' '세번째 줄')  # 튜플이 아닙니다.자료형은 문자
  print(str)

if (2 > 1):
  str = ("첫번째 줄 \n"
         '두번째 줄 \n'
         '세번째 줄')  # 튜플이 아닙니다.자료형은 문자

if (2 > 1):
  print("str", str)

if (2 > 1):
  print("".join(["첫번째 줄 \n", '두번째 줄 \n', '세번째 줄']))
