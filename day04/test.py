#Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#Q2

class MaxLimitCalculator(Calculator):
   def add(self, val):
        self.value += val

        if self.value > 100:
         cal1.value = 100


cal1 = MaxLimitCalculator()
cal1.add(50)
cal1.add(60)
print(cal1.value)

#Q3

print(all([1,2,abs(-3)-3]))
print(chr(ord('a')) == 'a')

#Q4

print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))

#Q5

print(int('0xea',16))

#Q6

print(list(map(lambda x: x*3,[1,2,3,4])))

#Q7

va1 = [-8,2,7,5,-3,5,0,1]
va2 = max(va1)+min(va1)
print(va2)

#Q8

print(round(17/3,4))

#Q9
#디렉터리 이동하고 파일 목록 출력하기

#Q10
#파일 확장자가 .py인 파일만 찾기

#Q11

import time
cur2 = time.strftime('%Y', time.localtime(time.time()))
cur1 = time.strftime('%X', time.localtime(time.time()))
cur3 = time.strftime('%m', time.localtime(time.time()))
cur4 = time.strftime('%d', time.localtime(time.time()))

print(f'{cur2}/{cur3}/{cur4} {cur1}')

#Q12
import random

result =[]



while True:
    valll = random.randint(1,45)
    while valll not in result:
        result.append(valll)
        
    if len(result) == 6:
        break

    result.sort()
    
print(result)

#Q13

import datetime

day1 = datetime.date(1995,11,20)
day2 = datetime.date(1998,10,6)

print(day2-day1)

#Q14

data=[('윤서현', 15.25),('김예지', 13.31),('박예원',15.34),('송순자',15.57),('김시우',15.48)]

from operator import itemgetter

result = sorted(data, key = itemgetter(1))
print(result)

#Q15

import itertools

print(list(itertools.combinations(['나지혜','성성민','윤지현','김정숙'],2)))

#Q16



print(print(list(itertools.permutations(['a','b','c','d'],4))))

#Q17


var1 = ['김승현','김진호','강춘자','이예준','김현주']
var2 = ['청소','빨래','설거지']



var3 = itertools.zip_longest(random.sample(var1,len(var1)),var2,fillvalue = '휴식')
print(list(var3))

#Q18
import math
varr1 = math.gcd(200,80)


print(varr1,int((200/varr1)*(80/varr1)),'개')

