# _01
a = "life is too short, you need python"

if "wife" in a:
  print("wife")
elif "prthon" in a and "yon" not in a:
  print("python")
elif "shirt" not in a:
  print("shirt")
elif "need" in a:
  print("need")
else:
  print("none")

# _02
result = 0
i = 1
while i <= 1000:
  if i % 3 == 0:
    result += i
  i += 1
print(result)

# _03
i = 0
while True:
  i += 1
  if i > 5: break
  print('*' * i)

# _04
for i in range(1, 101):
  print(i)

# _05
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in a:
  total += score
  # total = sum(a) # 합 구하는 함수
average = total / len(a)

import statistics
average = statistics.mean(a)
# print(average)
print(f"total: {total}\naverage: {average}")

# _06
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
  if n % 2 == 1:
    result.append(n * 2)
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]

fruits = ["사과","자두",'초콜렛',"바나나","체리"]
output = [fruit for fruit in fruits if fruit != '초콜렛']
print(result)
