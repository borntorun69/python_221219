import random

choice = random.random()
choice = random.randint(1, 100)
print(choice)

set_a = set([1,2,3]) # []를 set으로 변환
set_b = {1,2,3} # set을 직접 선언할때
lotto = set() # 비어 있는 set을 선언
while len(lotto) < 6:
  ball = random.randint(1, 45)
  lotto.add(ball)
lotto = sorted(lotto)
print(list(lotto))

lotto = []
for i in range(1, 46):
  lotto.append(i)
print(lotto)
# shuffle
for i in range(45):
  rand = random.randint(0, 44)
  lotto[i], lotto[rand] = lotto[rand], lotto[i]
print(lotto)

random.shuffle(lotto)
print(lotto)


# def main():
#   numbers = set()
#   while len(numbers) < 6:
#     numbers.add(random.randint(1, 45))
#
#   numbers = list(numbers)
#   numbers.sort()
#   print(numbers)
#
# if __name__ == '__main__':
#   main()

def main():
  lotto = []
  for i in range(1, 46):
    lotto.append(i)

  for i in range(45):
    rand = random.randint(0, 44)
    lotto[i], lotto[rand] = lotto[rand], lotto[i]

  for i in range(0, 45, 6):
    print(lotto[i:i+6])

if __name__ == '__main__':
  main()