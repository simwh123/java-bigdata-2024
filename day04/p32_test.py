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


#Q10

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
total = []


while True:
    valll = random.randint(1,45)
    while valll not in result:
        result.append(valll)
        
    if len(result) == 6:
        break

    result.sort()
    total.append(result)
    result =[]

print(total)