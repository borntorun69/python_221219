
class Terran:
  tribe = 'Terran'

class Marine(Terran):
  #클래스 변수(공통의 속성)
  name = 'Marine'
  __count = 0
  __attack_lv = 6
  __deffence_lv = 0

  #클래스 메서드
  @classmethod
  def get_count(cls):
    print(cls.__count, '※cls는 Marine과 동일')

  @property
  def hp(self):
    return self.__hp

  def __init__(self):
    self.__hp = 40
    # self.count += 1 #count는 인스턴스변수가 된다
    Marine.__count += 1
    print('생성되었습니다')
  # 더 사용할일 없는 데이터일 경우, 가비지컬렉터가 제거
  def __del__(self):
    Marine.__count -= 1
    print('소멸되었습니다')
  def move(self):
    Marine.get_count()
    print(f'{Marine.name} 가 이동합니다')

  def set_hp(self, hp):
    if hp < 0:
      raise TypeError("양의 정수를 넣으세요")
      self.__hp = hp

  def get_hp(self):
    return self.__hp

  @hp.setter
  def set_hp(self, hp):
    if hp > 0:
     self.__hp = hp
    else:
      raise TypeError("양의 정수를 넣으세요")

  @hp.getter
  def get_hp(self):
    return self.__hp

marines =[
  Marine(),Marine(),Marine(),Marine()
]

# print(Marine.__count)
marines[0].move()
Marine.get_count()
marines[0].get_count()
# marines[0].hp = -10
# Marine[0].hp = 100
print(marines[0].hp)
# print(marines[0].__hp)