# file : p25_test.py
# desc : 되새김 문제

# Q1
def is_odd(number):
    if number % 2 ==0:
        return True
    else:
        return False


# Q2
def avg_numbers(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result / len(numbers)

print(f'{avg_numbers(1,2)}')
print(avg_numbers(1,2,3,4,5))


# Q3
input1 = int(input('첫 번째 숫자를 입력하세요: '))
input2 = int(input('두 번째 숫자를 입력하세요: '))
print(f'두 수의 합은 {input1+input2} 입니다.')
# Q4

print('you''need''python')
print('you'+'need'+'python')
print('you','need','python')
print(''.join(['you','need','python']))

# # Q5

# f1 = open('test.txt','w')
# f1.write("Life is too short")
# f1.close()

f2 = open('test.txt','r')
print(f2.read())

# Q6

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt',mode= 'a',encoding='utf-8')
f.write('\n')
f.write(user_input)
f.close