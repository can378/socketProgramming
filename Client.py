import socket

# 서버의 IP 주소와 포트 번호 설정
SERVER_IP = '172.30.1.57'  # 서버의 IP 주소
SERVER_PORT = 5555  # 포트번호 설정 (서버와 동일)

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f'서버에 연결되었습니다. 서버 IP: {SERVER_IP}, 포트: {SERVER_PORT}')

while True:
    # 서버에게 데이터 전송
    message = input('전송할 메시지: ')
    client_socket.send(message.encode())

    # 서버로부터 데이터 수신
    data = client_socket.recv(1024)
    print(f'서버로부터 받은 데이터: {data.decode()}')

# 연결 종료
client_socket.close()
