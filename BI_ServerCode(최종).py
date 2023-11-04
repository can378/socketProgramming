import socket
import pandas as pd

df = pd.read_csv('BI.csv', header=None, encoding = 'utf-8')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.30.1.55', 12345))
server_socket.listen(5)

print("서버가 시작되었습니다. 클라이언트를 기다립니다...")

while True:
    client_socket, addr = server_socket.accept()
    print("클라이언트가 연결되었습니다.")
    while True:
        request = client_socket.recv(1024).decode()
        if request == "1":
            column_data = df.iloc[1:2, 0]
            for row in column_data:
                client_socket.send((row + '\n').encode('utf-8'))
        elif request == "2":
            column_data = df.iloc[1:2, 1]
            for row in column_data:
                client_socket.send((row + '\n').encode('utf-8'))
        elif request == "3":
            column_data = df.iloc[1:2, 2]
            for row in column_data:
                client_socket.send((row + '\n').encode('utf-8'))
        else:
            client_socket.send("올바른 요청이 아닙니다.".encode())
            continue

        continue_option = client_socket.recv(1024).decode()
        if continue_option != 'y':
            print("클라이언트와의 연결을 종료합니다.")
            break
    
client_socket.close()    
server_socket.close()
