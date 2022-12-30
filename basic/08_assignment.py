# 변수는 객체이다.
# 변수는 할당된다. call by reference 방식
s1 = 'hello'
s2 = 'world'
s3 = 'hello'
s4 = str('hello')
print(id(s1))
print(id(s2))
print(id(s3))
print(s1 is s4)
print('isalnum():', "TrainA10".isalnum())
print('isalpha():', "TrainA10".isalpha())
print('isidentifier():', "TrainA10".isidentifier())
# print('isidecima():', "3.141592".isidecima()) #소숫점 안됨
print('isdigit():', "3.141592".isdigit()) #소숫점 안됨
print('isspace():', " ".isspace()) #''," "는 안됨
print('islower():', " ".islower()) #''," "는 안됨
print('isupper():', " ".isupper()) #''," "는 안됨







i1 = 10
i2 = 10
print(i1, id(i1))
print(i2, id(i2))  # 숫자열 경우 값도 동일한 주소가짐

a = [1, 2, 3]
print(a, id(a))
b = a  # shallow copy : 주소를 복사(종속적)
print(b, id(b))
a.append(4)
print(a, b)

from copy import copy

c = a[:]  # deep copy : 데이터만 복사(독립적)
c = copy(a)  # deep copy : 데이터만 복사
c = [1, 2, 3, 4]  # deep copy : 데이터만 복사
print('**', a, id(a))
print('**', c, id(c))
a.append(5)
print(a, id(a))
print(c, id(c))
print()

print(f'{"변수 선언의 다른 방법":=^20}')
x, y = ('hello', 'world')  # tuple로 변수 선언
x, y = 'hello', 'world'
(x, y) = 'hello', 'world'
(x, y) = ('hello', 'world')

x, y = ['hello', 'world']  # list로 변수 선언
x, y = 'hello', 'world'
[x, y] = 'hello', 'world'
[x, y] = ['hello', 'world']

print(x, y)

a = b = 10
print(a, b)

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)
