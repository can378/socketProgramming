import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.16.196', 1234))

while True:
    request = input("원하는 정보를 선택하세요 (역사 : 1, 지표 : 2, 경기방식과 기본 규칙 : 3): ")
    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode('utf-8')

    if "올바른 요청이 아닙니다." in response:
        print(response)
        continue
    else:
        print("해당 정보를 제공해드리겠습니다:")
        print(response)

    continue_option = input("다른 정보도 궁금하시면 y, 종료하시려면 n을 입력해주세요.")
    client_socket.send(continue_option.encode())
    if continue_option.lower() != 'y':
        break

client_socket.close()
