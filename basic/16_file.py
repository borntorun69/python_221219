print("Life" "is" "Good")
print("Life"+"is"+"Good")
print("Life","is","Good")

#open 할때 3가지 모드 r, w, a
f = open('./hello.txt','r')
while True:
  line = f.readline()
  if not line: break
  print(line)
f.close()

f = open('./hello.txt','w')
str = 'Happy New Year \n'
f.write(str)
f.close()

f = open('./hello.txt','a')
str = '건강하세요 \n'
f.write(str)
f.close()

with open('./hello.txt','w') as f:
  f.write("with File")



def fopen(filename):
  f = open(filename, 'r')
  lines = f.readlines()
  for line in lines:
    print(line)
  f.close()

def fwrite(filename,str):
  with open(filename,'w') as f:
    f.write(str + "\n")
def fappend(filename,str):
  with open(filename,'w') as f:
    f.write(str + "\n")


fwrite('./hello.txt',fappend)
fappend('./hello.txt',fappend)
fopen('./hello.txt')



