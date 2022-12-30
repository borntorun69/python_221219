# list  순서 있고 중복 허용, muttable

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_a = ['Life', 'is', 'Good', 'and', 'Happy']
list_a = ['홍길동', '90', '100', '90']

print('list_a: ', list_a)
print(list_a[0])
for item in list_a:  print(item)

for i in range(0, len(list_a)):
  print(str(i) + ")", list_a[i])

print(list_a[1:30])
# print(list_a[30]) #범위 밖 error

print(list(range(0, 10)))

list_a[0] = '고길동'  # list는 muttable 자료형.
# print(list_a)

lists = [
  ['홍길동', '90', '100', '90'],
  ['고길동', '91', '90', '90'],
  ['강길동', '89', '95', '90'],
  ['김길동', '70', '92', '90'],
]
print(lists)
print(lists[0])
print(lists[1][3])

for i in range(0, len(lists)):
  hap = 0
  for j in range(0, len(lists[i])):
    if j != 0:
      print(",", end="")
      hap += int(lists[i][j])
    # print("%3s" % lists[i][j], end="")
    print("{0:>3}".format(lists[i][j]), end="")
    # print(f"{lists[i][j]:>3s}", end="")
  print(", %3d" % hap)

# 2차원 list 크기 초기화
lists2 = [[0 for col in range(5)] for row in range(5)]

for i in range(0, len(lists)):
  for j in range(0, len(lists[i])):
    lists2[i][j] = lists[i][j]
    if j != 0:
      lists2[i][len(lists[i])] += int(lists[i][j])
      lists2[len(lists)][j] += int(lists[i][j])
      lists2[len(lists)][len(lists[i])] += int(lists[i][j])

for i in range(0, len(lists2)):
  for j in range(0, len(lists2[i])):
    if j != 0:
      print(",", end="")
    if i == len(lists2) - 1 and j == 0:
      lists2[i][j] = "합계"
      print("{0:^6}".format(lists2[i][j]), end="")
    else:
      print("{0:>5}".format(lists2[i][j]), end="")

  print()

a = [1, 2, 3]
b = list(range(3, 7))  # list()와 range()로 list생성
print(a, ', ', b)

print(a + b)  # 합
print(b + a)
c = a + b
c = b + a
print(c)
print(a * 3)

print(len(a))
b[0] = 0  # 수정
print(b)

del b[0]  # 삭제 indexing
print(b)

del b[:1]  # 삭제 slicing
print(b)

print(f'{" list 함수 ":=^20}')
b.append(4)
b.sort()
print(b)
list_a = ['Life', 'is', 'Good', 'and', 'Happy']
list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)
print(list_a.index('Life'))
print(c.index(3))
print(c)
a.insert(0, 4)
print(a)
a.insert(20, 6)  # list 인덱스가 넘으면 끝자리에 반영.
a.insert(2, 6)
print(a)
a.remove(6)  # 리스트에서 첫번째 만나 것을 지움.
print(a)
a.pop()  # pop: args 없을 때 끝요소 리턴과삭제
print(a)
a.pop(0)  # pop: args 있을 때 지정요소 리턴과삭제
print(a)
print(a.count(1))
print(c, c.count(3))

d = []
# d.extend(a)
d += a
print(d)
print(1 in d)
print(1 not in d)

d.clear()
print(d)
print()




