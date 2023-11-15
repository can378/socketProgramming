import socket

# 서버의 IP 주소, 포트 번호 설정
SERVER_IP = ' 1'
SERVER_PORT = 1233

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 버퍼 크기 설정 (예: 4MB)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 10 * 1024 * 1024)

# 서버에 연결
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f'서버에 연결. 서버 IP: {SERVER_IP}, 포트: {SERVER_PORT}')

homeMenuExplain="\n\n==== 원하는 숫자를 선택하세요.\n==== 1.성적예측  2.경기조회  3.선수조회  4.야구퀴즈  5.야구상식  6.종료\n"
print(homeMenuExplain)

while True:
    try:
        message = input("선택: ")
        message_byte = str(int(message)).encode()
        client_socket.send(message_byte)

        if message == '4':
            for _ in range(10):
                question = client_socket.recv(1024).decode()
                print(question)
                add_input = input("정답 입력: ")
                add_input_byte = add_input.encode('utf-8')
                client_socket.send(add_input_byte)
                result_message = client_socket.recv(1024).decode()
                print(result_message)
    except ValueError:
        print("해당 번호를 입력하세요.")
        continue
       
    # 서버로부터 데이터 수신
    data = client_socket.recv(10 * 1024 * 1024)
    print(data.decode())

# 연결 종료
client_socket.close()
