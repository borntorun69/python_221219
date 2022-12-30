# 자료형(변수)의 종료
# 기본 자료형 (bool,int,float,str의 class type )
# 숫자형 (정수형, 실수형
# 문자열

# 변수명 규칙
# 에약어 안됨
# _. 영문자 시작(숫자 안됨)
# 특수문자,공백 안됨
# Comelcase는 변수나 함수의 적용

print("# 숫자형 int, float")
a = 10
print(a)
print(type(a))
a = 10.234
a = 0B101  # 0B 또는 0b 로 시작하는 2 진수
a = 0o12  # 0o 또는 0O 로 시작하면 8 진수
a = 0x2a  # 0X 또는 0x 로 시작하면 16진수
a = 123e2  # en 또는 En 로 시작하면 10제곱승
a = 123E-2
print(a)
print(type(a))
print()
# 10진수를 2진수로 변경
print('10 -> 2진수:', bin(10))
# 10진수를 8진수로 변경
print('10 -> 8진수:', oct(10))
# 10진수를 16진수로 변경
print('10 -> 16:', hex(10))

# 2진수를 10진수로 변경
print('101 -> 10진수:', int('0101', 2))
# 8진수를 10진수로 변경
print('017 -> 10진수:', int('017', 8))
# 16진수를 10진수로 변경
print('a1 -> 10진수:', int('a1', 16))
print()

print(format(10, 'b'))
print(format(10, '0'))
print(format(10, 'x'))
print(format(10, 'x'))
print(format(10, 'd'))
print(format(10, '#b'))
print(format(10, '#o'))
print(format(10, '#x'))
print(format(10, '#x'))
print(format(10, 'd'))

print("#사칙 연산 +,-,*,/", end="::")
b = 10;
c = 20;
print(b + c);
print("# 몫 연산자 //", end="::")
print(3 / 2, 3 // 2)
print("#나머지 연산자 %", end="::")
print(3 % 2)
print("#제곱 연산자 **", end="::")
print(3 ** 2, 10 ** 3)
print("#비트 연산자 &", end="::")
print(bin(0b010 & 0b101))
print("#비트 연산자 |", end="::")
print(bin(0b010 | 0b101))
print("#비트 연산자 ^", end="::")
print(bin(0b010 ^ 0b101))
print("#비트 연산자 ~", end="::")
print(bin(~ 0b101))

print("# shift 연산자 >><<")
print("%s << %s => " % (bin(2), bin(2 << 2),))

print("# 비교연산자(>,<,>=,<=,!=)와 논리 연잔자(and,or,not")
power = True
print(power, type(power), sep=",")
print((power or 3 < 1) and 2 < 1 or power)
print(not power)
print()

print("# 문자열 str")
a = "Hello Python"  # 쌍따옴표,홑따옴표 모두 문자열
print(type(a))
# a[1] = 'a'  쓸수 없다

print(a + "Hello world")  # 타빙이 같음
# print(a + 123) # TypeError 발생:타입이 다름

print("go" * 3)
print("Hello python"[0])  # indexing 시작은 0부터
print("Hello python"[-1])  # indexing 시작은 끝부터 -1
# print("Hello python"[20]) #IndexError: string index out of range

print("Hello python"[0:4])  # slicing 끝 글자는 미포함
print("Hello python"[6:])  # slicing 6부터 끝까지
print("Hello python"[:5])  # slicing 0~4까지
print("Hello python"[0:20])  # slicing 에러 무발생

print(len("Hello python"))

print("I eat %s" % 'apple')
print("I eat %d %s" % (3, 'apple'))
ch = 'a'
print("%s of Asccii code is %d" % (ascii(ch), ord(ch)))
print("%d is %s" % (ord(ch), chr(ord(ch))))
print((ascii('''

\n


''')))
print(ord('\n'))
num = 10
print("%d의 8진수는 %o,16진수는 %x" % (num, num, num))
print(('%c 는 문자 1개입니다.' % 'z'))
print('Error is %d%%' % 98)  # 몇 % 표시할때 %%사용
print("%10s" % 'hi')
print("%-10s " % 'hi')
print('%0.4f' % 3.141592)  # 끝자리는 반올림됨
print('%10.4f' % 3.141592)  # 10은 총자릿수(점포함)
print("I eat {0}".format('Apple'))  # 1개의 값 넣기
print("I eat {0} {1}".format(3, 'Apple'))  # 2개이상 값 넣기
print("I eat {num} {item} ".format(num=3, item='Apple'))  # 2개의 값 넣기
print("I eat {0} {item}".format(3, item='Apple'))  # 2개의 값 넣기
print(num)

print(f'{".format() 함수":=^20}')
print('{} {} {}'.format(10,20,30)) #중괄호의 갯수 = 변수갯수
print("{:+d}".format(52)) #+52
print("{:d}".format(-52)) #-52
print("{:+5d}".format(52)) #__+52,부호가 숫자 바로 앞에 위치
print("{:5d}".format(-52)) #__-52
print("{:=+5d}".format(52)) #+__52,부호가 줄의 앞에 위치
print("{:=5d}".format(-52)) #-__52
print("{:+05d}".format(52)) #+0052,빈자리를 0으로 채움
print("{:#5d}".format(-52)) #__-52, 빈자리를 #(공백)으로 채움
print("{:f}".format(52.273))     #52.273000
print("{:15f}".format(52.273))   #______52.273000
print("{:+15f}".format(52.273))  #_____+52.273000
print("{:-015f}".format(52.273)) #00000052.273000



print("({0:=^20})".format('format '))
print("({0:<10})".format('hi'))  # 왼쪽정렬
print("({0:>10})".format('hi'))  # 오른쪽정렬
print("({0:^10})".format('hi'))  # 중앙정렬
print("({0:0>10})".format('10'))
print("({0:0.4f})".format(3.141592))
print("({0:10.4f})".format(3.141592))
print("{{}}는 클래스이다".format())

print(f'{" f ":=^20}') #변수 선언시 사용가능
city = 'Busan'
print(f"나의 살던 고향은 '{city}' '부산'")
print(f"나의 살던 고향은 \"{city}\" '부산'")
d = {'city': '부산', 'gu': '부산진구'}  # 딕셔너리 활용
print(f"내가 일하는 곳 \"{d['city']} {d['gu']}\"")
print(f"({3.141592:0.4f})")
print(f"({3.141592:10.4f})")
print(f"{{}}는 클래스이다")

print(f'{"기타 문자열 함수":=^20}')
print("hello world".count('l'))
print("hello world".find('l'))  # 없으면 -1 반환
print("hello world".rfind('l'))  # 없으면 -1 반환
print("--"*20)


print("hello world".index('l'))  # 없으면 error발생
print(",".join('12345'))
print('hello'.upper())
print('WORLD'.lower())
print('hello world'.capitalize())  # 첫글자만 대문자
print('hello world'.split(' '))
l = 'hello world'.split() #split후에는 list자료형이 온다
for i in l:
    print(i.capitalize(), end=" ")
print()
print('  strip world  '.strip())
print('  strip2 world  '.lstrip())
print('  strip3 world  '.rstrip())

