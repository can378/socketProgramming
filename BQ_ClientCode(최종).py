import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.4", 12345))

print("서버에 연결되었습니다.")

while True:
    for _ in range(10):
        question = client_socket.recv(1024).decode()
        print(question)

        user_answer = input("답변을 입력하세요:")
        client_socket.send(user_answer.encode())

        response = client_socket.recv(1024).decode()
        print("출제자:", response)

    result_message = client_socket.recv(1024).decode()
    print("게임 결과:", result_message)

    play_again = input("게임을 다시 시작하시겠습니까? (y/n): ")
    client_socket.send(play_again.encode())
    if play_again.lower() != 'y':
        break
    
client_socket.close()
    
