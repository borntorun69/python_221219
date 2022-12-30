# bool True, False

a = True
print(type(a))

print(f'{"자료형의 참과 거짓":=^20}')
print(1, bool(''))  # 문자열
print(2, bool('hello'))
print(3, bool([]))  # list
print(4, bool([1]))
print(5, bool([1]))  # tuple
print(6, bool((1,)))
print(7, bool(0))  # int
print(8, bool(-123124))  # 0은 음수, 0 제외한 정수는 모두양수
print(9, bool(0.0))
print(10, bool(-0.1234))  # 0은 음수, 0 제외한 정수는 모두양수
print(11, bool({}))  # dict
print(12, bool({'n1': 10, 'n2': 20}))
print(13, bool(set([])))
print(14, bool(set([1, 2, 3])))
print(15, 2 > 1)  #비교연산자
print(16, bool(1 and 0 or 0 and 1))

a=[1,2,3,4]
while a:
  print(a.pop(),end='')