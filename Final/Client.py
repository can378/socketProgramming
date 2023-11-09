import socket

# 서버의 IP 주소, 포트 번호 설정
SERVER_IP = '192.168.16.196'
SERVER_PORT = 1233

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f'서버에 연결. 서버 IP: {SERVER_IP}, 포트: {SERVER_PORT}')





while True:
    
    client_socket.send("0".encode('utf-8'))
    
    # 서버로부터 데이터 수신
    while True:
        data = client_socket.recv(1024)
        if data.decode()=="end": break
        else: print(data.decode())
    
    
    # 서버에게 데이터 전송
    message = input('번호 선택: ')
    client_socket.send(message.encode())

   
    

# 연결 종료
client_socket.close()
