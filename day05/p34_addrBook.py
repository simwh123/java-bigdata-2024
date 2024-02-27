# file: 034_addrBook.py
# desc: 콘솔 주소록 프로그램

class Contact:  # 주소록 클래스
    __name = ''
    __phoneNumber = ''
    __eMail = ''
    __addr = ''

    # 생성자
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr
    
    # 사용자가 원하는 형태로 출력
    def __str__(self) -> str:
        res = (
f'''이  름 : {self.__name} 
핸드폰 : {self.__phoneNumber} 
이메일 : {self.__eMail} 
주  소 : {self.__addr} ''')
        return res

def run():
    first = Contact(addr ='경성',phoneNumber='010-9999-5555',name='홍길동',eMail='hgd@navere.com')
    print(first)


if __name__ == '__main__':  # 메인엔트리
    print('프로그램 시작')
    run() # 메인함수 실행

print('프로그램 종료')