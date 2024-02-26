# file: p26_exceptionHandle.py
# desc: 예외처리
# 오류(Error) : 코드상 빨간색(노란색) 밑줄이 그어지는 것
# 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 1. 파일읽기
try:
    f = open('./sanple.txt', mode = 'r', encoding = 'utf-8')
    # blah blah blah
    res = f.readline()
    print(res)
except:
    print('파일오픈 예외발생!!')
else: # 예외가 없을때 실행
    f.close()
    
#finally:
#    try:    # try~except는 다중으로 사용하면 성능에 별로 안좋다
#        f.close()   # f에 파일 객체자체가 없어서 close()불가 
#    except:
#        print('파일 오픈 실패')

# 2. 계산결과
try:    
    print(5/0)
except ZeroDivisionError as e:
    print('0으로 나눌수 없습니다.',e.args)

# a, b = 5, 3

# if a == b:
#    print(True)
