

import random

def main():
  numbers = []
  while len(numbers) < 6:
    number = random.randint(1, 45)
    if number not in numbers:
      numbers.append(number)

  numbers.sort()
  print(numbers)

if __name__ == '__main__':
  main()

def main():
  numbers = set()
  while len(numbers) < 6:
    numbers.add(random.randint(1, 45))

  numbers = list(numbers)
  numbers.sort()
  print(numbers)

if __name__ == '__main__':
  main()