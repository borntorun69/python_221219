# set 중복불허, 순서없다

s1 = set("Hello")
print(s1)
for item in s1:
  print(item,end='')
print()

l1 = sorted(s1)
for item in l1:
  print(item, end='')
print()

print(f'{"합집합,교집합,차집합 구하기":=^30}')
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print('합집합',s1 | s2, s1.union(s2))
print('교집합',s1 & s2, s1.intersection(s2))
print('차집합',s1 - s2, s1.difference(s2))

s1 = set([1,2,3])
s1.add(4); s1.add(4);
print(s1)

s1.update([4,5,6])
print(s1)

# s1.remove(7) #없으면 keyError
s1.remove(6)
print(s1)


