# tuple ()로 정의, 순서있고, 중복허용, Immtuable(생성, 삭제, 수정이 안됨)
ti = ()
t2 = (2)  # type은 int가 됨 tuple아님
t2 = (1,)  # tuple에서 1개 자료만 있는 경우 뒤에 ,를 직어라
t3 = (1, 2)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(type(t4))

print(t5)

for item in t5:
  print(item, end='')
print()
for i in range(0, len(t5)):
  print(i, t5[i], sep=")", end='')
print()

# t4[0] = 0: #immutable type
# del t4[0]: #immutable type

t1 = tuple(range(10))
t1 = tuple(range(2, 10))
print(len(t1))
t1 = ((0 for col in range(5)) for row in range(5))

print(f'{"이중 for문 ":=^20}')
for r in t1:
  idx = 0
  for item in r:
    if idx != 0:
      print(",", end='')
    idx += 1.
    print(f"{item:>2d}", end='')
  print()

# for i in range(0,len(t1)):
#   for j in range(0, len(t1[i])):
#     print(f"{item:>2d}",end="")

t1 = (1, 2, 'a', 'b')
print(t1[2])  # tuple indexing
print(t1[:2])  # tuple slicing
t2 = 3, 4,
print(t1 + t2)
t1 = t1 + t2
print(t1)  # tuple을 합친게 아니고 재정의 함

print(len(t1))
print(t1 * 2)
