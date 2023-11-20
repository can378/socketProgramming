import socket

# 서버의 IP 주소, 포트 번호 설정
SERVER_IP = '172.30.1.1'
SERVER_PORT = 1233

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f'서버에 연결. 서버 IP: {SERVER_IP}, 포트: {SERVER_PORT}')

homeMenuExplain="\n\n==== 원하는 숫자를 선택하세요.\n==== 1.성적예측  2.경기조회  3.선수조회  4.야구퀴즈  5.야구상식  6.종료\n"
print(homeMenuExplain)




while True:
    
    
    # 사용자로부터 입력 받기
    user_name = input("사용자 이름: ")
    password = input("비밀번호: ")
    
    # 메시지 구성
    service_code = b'\x01'  # 0x01을 바이트로 표현
    user_name_bytes = user_name.encode('utf-8')
    password_bytes = password.encode('utf-8')
    
    # 전체 메시지 구성
    message = service_code + user_name_bytes + b' ' + password_bytes

    message=message.replace(" ","")
    client_socket.send(message)
    
    
    
    # 서버로부터 데이터 수신
    data = client_socket.recv(10 * 1024 * 1024)
    print(data.decode())
    




# 연결 종료
client_socket.close()






