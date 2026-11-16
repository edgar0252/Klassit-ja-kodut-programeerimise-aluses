
import time

time.sleep(3)
print("hello")

import datetime as d
print(d.datetime.now())
print(d.datetime.now().date())
print(d.datetime.now().time())
print(d.datetime.now().time().hour)
print(type(d.datetime.now().time().hour))

import sys, os, platform


print(sys.path)
print(os.name)
print(platform.system())

from math import sqrt as s


print(s(100))


#import mymodle as my

#print(my.name)
#my.hello()

from mymodle import add_three_numbers as addi

print(addi(1,4,0))
