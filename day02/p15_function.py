# file: p15_function.py
# desc: 함수 학습

def plus(a, b): # 매개변수, 리턴값 O
    res = a + b
    return res

def miuns(a, b): # 매개변수, 리턴값 x
    res = a-b
    print(res)

def multi(): # 매개변수X, 리턴값O
    global a, c # 밖에 있는 전역변수 a, c 를 사용하겠다
    res = a*c
    return res

def divide():
    global a,c
    print(a /c)

def pow(a,b):
    res = a**b
    return res

print('더하기')
a = 10
c = 7
result = plus(a,c)
print(result)

miuns(a,c)
result = multi()
print(result)
