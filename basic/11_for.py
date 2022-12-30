# for
#
# for i in range(2, 10):
#   for j in range(1, 10):
#     # print("%d*%d=%2d" % (i,j, i*j))
#     # print("{0}*{1}={2}".format(i,j,i*j))
#     # print(i, "X", j, "=", i * j)
#     print(f"{i} X {j} = {(i * j):>2}")
#   print()
n = 3
for i in range(2, 10, n):
  for j in range(1, 10):
    for k in range(i, i + n):
      if (k != 10):
        print(f"{k} X {j} = {(k * j):>2}\t", end='')
    print()
  print("-" * 50)

import time
for i in range(10,-1,-1):
  print(i)
  time.sleep(1)





