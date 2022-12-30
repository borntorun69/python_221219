class Calculator:
  n3 = 100
  def __init__(self,n1=1, n2=1):
    self.n1 = n1
    self.n2 = n2
  def setdata(self, n1, n2):  # self 자신을 가리킴, setdata속성
    if n1 > -1: self.n1 = n1
    self.n2 = n2
  def add(self):
    return self.n1 + self.n2
  def add(self):              #메서드 중복시 마지막정의가 우선
    return self.n1 + self.n2 + self.n3
  def sub(self):
    return self.n1 - self.n2
  def mul(self):
    return self.n1 * self.n2
  def div(self):
    return self.n1 / self.n2
  def selfish(self):
    print('parent')

c1 = Calculator()
c2 = Calculator()
c3 = Calculator(3,4)

c3.n3 = 200
print(type(c1))
print(id(c1))
print(id(c2))

Calculator.setdata(c1, 4, 2)
# c1.setdata(4,2)
c2.setdata(2, 1)

print(c1.n1, c1.n2, c1.n3)
print(c2.n1, c2.n2,c1.n3)
print(c3.n1, c3.n2, c1.n3)

print(id(c1.n1))
print(id(c2.n2))

print(c1.add())
print(c1.add())

class MultiCalc(Calculator):
  n3 = 300
  def setdata(self, n1, n2, n3 = 200):  # self 자신을 가리킴, setdata속성
    if n1 > -1: self.n1 = n1
    self.n2 = n2
    self.n3 = n3
  def selfish(self):
    print('child')

# 상속시 인스턴스변수가 중복될 경우 자손값
# 상속시 클래스변수이면서  중복될 경우 자손값
# 상속시 메서드명 상속할 경우 자손을 따름
m1 = MultiCalc(10,20)
print(m1.add())
# print(m1.setdata())
print(m1.n3)

m1.selfish()

m2 = Calculator();
