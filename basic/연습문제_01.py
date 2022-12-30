# 01
k = 80
e = 75
m = 55
print('01) 평균', (k + e + m) / 3)

# 02
# num = int(input("숫자 입력(0은 종료)"))
# coka = num%2
# if coka:
#   print('02)',"홀수")
# else:
#   print('02)',"짝수")
# print('홀수' if coka else '짝수')  #삼항 연산자

# 03
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print('03)', yyyymmdd)
print('03)', num)

# 04
se = pin[7:8]
print('04)', '남성' if pin[7:8] == 1 else '여성')

# 05
# a = "a:b:c:d"
# b = a.replace(':', '#')
# print('05)', b)
print("a:b:c:d".replace(':', '#'))

# 06
a = [1, 3, 5, 4, 2]
a.sort()
print('06)', a)
a.reverse()
print('06)', a)

# 07
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print('07)', result)

# 08
a = (1, 2, 3,)
a = a + (4,)
print('08)', a)

# 09
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' #TypeError: unhashable type: 'list'
a[250] = 'python'
for key in a:
 print('09)', key, a[key])

# 10
a = {'A': 90, 'B': 80, 'C': 70}
result = a['B']
result = a.pop('B')
print(a)
print(result)

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = []
for i in a:
  if i not in aSet:
    aSet.append(i)
print(aSet)

# 12
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)

# a, b = [1, 2, 3] , [1, 2, 3]

# 이런식으로 선언하면 a 요소값이 변해도 b는 안변함