from my_util import *
# import mod1
from mod1 import *
import constant2 as const

linez("module::함수,변수,클래스를 모아둠")

print(add(3, 4))

print(PI)
print(GRAVITY)

PI = 3.14
print(PI)

const.PI = 3.14
const.GRAVITY = 9.86

print("constant2.PI:",const.PI)
# const.PI = 3.14 #엘러발생

