import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.16.196", 12346))

while True:
    menu = client_socket.recv(1024).decode()
    print(menu)
    
    user_input = input("원하는 기능의 번호를 선택하세요: ")
    client_socket.send(user_input.encode())

    if user_input == '4':
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

    elif user_input == '5':
        while True:
            request = input("원하는 정보를 선택하세요 (역사 : 1, 지표 : 2, 경기방식과 기본 규칙 : 3): ")
            client_socket.send(request.encode())

            response = client_socket.recv(2048).decode('utf-8')

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

    elif user_input == '6':
        print("서버와의 연결을 종료합니다.")
        client_socket.close()
        break


