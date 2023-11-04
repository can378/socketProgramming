import socket
import random

filename = r'C:\BQ.txt'
def load_questions(filename):
    with open(r'C:\BQ.txt', "r", encoding = "utf-8") as file:
        content = file.read()
    questions = content.split('# ')[1:]
    parsed_questions = []

    for question in questions:
        parts = question.split('\n')
        q_text = parts[0]
        correct_answer = parts[1].split(": ")[1]

        parsed_questions.append((q_text, correct_answer))

    return parsed_questions

# 서버 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("172.30.1.55", 12345))
server_socket.listen(5)

questions = load_questions(r"C:\BQ.txt")

print("서버가 시작되었습니다. 클라이언트를 기다립니다...")

while True:
    # 클라이언트 연결 대기
    client_socket, addr = server_socket.accept()
    print("클라이언트가 연결되었습니다.")
    selected_questions = []

    while True:
        # 맞춘 개수 초기화
        correct_count = 0

        if len(selected_questions) == 0:
            selected_questions = random.sample(questions, 10)

        for question, correct_answer in selected_questions:
            client_socket.send(question.encode())
            client_answer = client_socket.recv(1024).decode()
    
            if client_answer.lower() == correct_answer.lower():
                correct_count += 1
                response = "정답입니다!"
            else:
                response = f"틀렸습니다. 정답은 '{correct_answer}'입니다."

            client_socket.send(response.encode())


        # 맞춘 개수에 따른 메시지 전송
        if correct_count == 10:
            result_message = "모두 맞추셨습니다. 축하합니다!"
        elif correct_count >= 7:
            result_message = "7개 이상 맞추셨습니다. 잘 하셨어요!"
        elif correct_count >= 3:
            result_message = "3개 이상 맞추셨습니다. 더 분발하세요!"
        else:
            result_message = "하나도 못 맞추셨습니다. 계속 노력하세요!"
        client_socket.send(result_message.encode())

        play_again = client_socket.recv(1024).decode()
        if play_again.lower() != 'y':
            print("클라이언트와의 연결을 종료합니다.")
            break

# 연결 종료
client_socket.close()
server_socket.close()
