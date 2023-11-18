import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.30.1.57', 5000))
server_socket.listen(1)

print("서버 대기 중...")

while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024)

    if not data:
        break

    service_code = data[0]

    if service_code == 0x01:
        # 0x01인 경우, 로그인 요청으로 처리
        user_info = data[1:].decode('utf-8').split(' ')
        user_name = user_info[0]
        password = user_info[1]
        print(f"로그인 요청: 사용자 이름 - {user_name}, 비밀번호 - {password}")
    else:
        print("알 수 없는 서비스 코드:", service_code)

    client_socket.close()

server_socket.close()
