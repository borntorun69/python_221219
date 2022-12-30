import sys
print(sys.argv)

# sys.exit()

print('강제 종료되나요?')

print(sys.path)

import pickle
f = open('test.txt','wb')
data = {1:'python',2: 'tkinter'}
pickle.dump(data, f)
f.close()

f = open('test.txt','rb')
data = pickle.load(f)
print(data)

import os
os.chdir('c:')
print(os.getcwd())
f = os.popen("dir")
print(f.read())

import calendar
calendar.prmonth(2088,12)
print(calendar.monthrange(2023, 2))



