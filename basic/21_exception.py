# runtime error, syntax error

print(1)
try:
  print(2)
  f = open('xman', 'r')
  print([1, 2, 3][3])
  print(10 / 0)
  print(3)
except FileNotFoundError as e:
  pass  # 준비가 안된 경우
except IOError as e:
  print(4, 1, sep='-')
except (ZeroDivisionError, IndexError) as e:
  print(4, 1, sep='-')
except Exception as e:
  print(4)
finally:
  print(5)
print(6)

input_ans = input('숫자만 입력하세요')
if input_ans.isdigit():
  print(int(input_ans) + 100)
else:
  print('정수를 입력하세요')

try:
  print(int(input_ans) + 100)
except:
  try:
    print(int(input_ans.strip()) + 100)
  except:
    print('숫자를 입력하세요')


class Bird:
  def fly(self):
    raise NotImplementedError


class Eagle(Bird):
  # pass

  def fly(self):
    print("훨훨~~")


eagle = Eagle()
eagle.fly()

# 사용자 예외처리 클래스
class MyError(Exception):
  # pass
  def __str__(self):
    return "허용되는 않는 별명입니다"

def say_nick(nick):
  if nick == '바보':
    raise MyError()
  print(nick)

# say_nick('천사')
# say_nick('바보')

try:
  say_nick('천사')
  say_nick('바보')
except MyError as e:
  print(e)

class CustomException(Exception):
  def __init__(self):
    Exception.__init__(self)
  def __str__(self):
    return "오류가 발생했어요"

# raise CustomException()

class CustomException2(Exception):

  def __init__(self,message,value):
    Exception.__init__(self)
    self.message = message
    self.value = value
  def __str__(self):
    return "오류가 발생했어요"
  def print(self):
    print("#####오류 정보#####")
    print("메시지:",self.message)
    print("값:",self.value)

try:
  raise CustomException2("CustomException2",5)
except CustomException2 as e:
  e.print()