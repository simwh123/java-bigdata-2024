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
        res = (f'''이  름 : {self.__name} 
핸드폰 : {self.__phoneNumber} 
이메일 : {self.__eMail} 
주  소 : {self.__addr} ''')
        return res
def setContact():
    (name,phoneNumber,eMail,addr) = input('주소록 입력(이름, 핸드폰, 메일, 주소[구분자/]>)').split('/')
    name = name.strip()     #사용자실수로 들어간 스페이스 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    print(f'''"{name}"
"{phoneNumber}"
"{eMail}"
"{addr}"''')

def displayMenu():
    menu = ('''
            주소록 프로그램
            1. 연락처 추가
            2. 연락처 출력
            3. 연락처 삭제
            4. 종       료
            ''')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def run():
    while True:
        selMenu = displayMenu()
        if selMenu == 4:
            break


if __name__ == '__main__':  # 메인엔트리
    print('프로그램 시작')
    run() # 메인함수 실행

print('프로그램 종료')