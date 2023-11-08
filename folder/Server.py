import socket
import select

# 서버 IP 주소와 포트 설정
HOST = '172.30.1.57'  # 모든 네트워크 인터페이스에 바인딩
PORT = 12345  # 사용할 포트 번호

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 주소와 포트에 바인딩
server_socket.bind((HOST, PORT))

# 클라이언트의 연결 대기
server_socket.listen(1)
print('서버가 클라이언트 연결을 대기 중입니다...')

# 클라이언트 연결 수락
client_socket, client_address = server_socket.accept()
print(f'{client_address}에서 연결됨')

while True:
    # 클라이언트로부터 데이터 수신
    data = client_socket.recv(1024)
    if not data:
        break
    print(f'수신한 데이터: {data.decode()}')

    # 클라이언트에게 데이터 전송
    message = input('전송할 메시지: ')
    client_socket.send(message.encode())

# 연결 종료
client_socket.close()
server_socket.close()