
# 1) 각각의 객체를 만들 때
std1 = {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88}
std2 = {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88}
std3 = {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88}

# 2) 리스트와 딕셔러리를 객체를 만들때
students = [
  {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88},
  {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88},
  {"name": "홍길동", 'kor': 87, 'mat': 98, 'eng': 88}
]

# 3) 함수를 이용하여 객체를 만들때
def create_std(name, kor, mat, eng):
  return {"name": name, 'kor': kor, 'mat': mat, 'eng': eng, }

print("Name", "합", "Average", sep="\t")
for std in students:
  tt = std['kor'] + std['mat'] + std['eng']
  avg = tt / 3
  print(f"{std['name']:3s}, {tt:>4d}, {avg:>5.2f}")

# 4) 여러 함수를 이용하여 객체를 맍들때
def create_std(name, kor, mat, eng):
  return {"name": name, 'kor': kor, 'mat': mat, 'eng': eng, }

def get_sum(std):
  return std['kor'] + std['mat'] + std['eng']
def get_avg(std):
  return get_sum(std)/3

def get_std(std):
  return f"{std['name']:3s}, {get_sum(std):>4d}, {get_avg(std):>5.2f}"

students = [
  create_std('홍길동', 87, 98, 100),
  create_std('홍길동', 87, 98, 100),
  create_std('홍길동', 87, 98, 100),
]

print("Name", "합", "Average", sep="\t")
for std in students:
  print(get_std(std))

# 5) class 선언하기
class Student:
  def __init__(self, name, kor, mat, eng):
    self.name = name
    self.kor = kor
    self.mat = mat
    self.eng = eng
  def __del__(self):
    # print(f'{self.name}의 인스턴스를 제거하였습니다.')
    pass
  def get_sum(self):
    return self.kor+ self.mat+ self.eng

  def get_avg(self):
    return self.get_sum() / 3
  def to_string(self):
    return f'{self.name:^4s} {self.get_sum():>4d} {self.get_avg():>6.2f}'

  def __str__(self):
    return f'{self.name:^4s} {self.get_sum():>4d} {self.get_avg():>6.2f}'

  def __eq__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() == other.get_sum()

  def __ne__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() != other.get_sum()

  def __gt__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() > other.get_sum()

  def __lt__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() < other.get_sum()

  def __ge__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() >= other.get_sum()

  def __le__(self, other):
    if not isinstance(other, Student):
      raise TypeError("Student의 인스턴스가 아님니다.")
    return self.get_sum() <= other.get_sum()

students = [
  Student('홍길동', 87, 98, 100),
  Student('김길동', 87, 98, 100),
  Student('박길동', 87, 98, 100),
]

print("Name", "합", "Average", sep="\t")
for std in students:
  print(std.to_string())

print(students[0])
print(students[1])
print("__eq__ :",students[0] == students[1])
print("__ne__ :",students[0] != students[1])
print("__gt__ :",students[0] > students[1])
print("__lt__ :",students[0] < students[1])
print("__ge__ :",students[0] >= students[1])
print("__le__ :",students[0] <= students[1])



