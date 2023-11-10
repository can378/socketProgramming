import socket
import random
import pandas as pd

filename = r'BQ.txt'
def load_questions(filename):
    with open(r'BQ.txt', "r", encoding = "utf-8") as file:
        content = file.read()
    questions = content.split('# ')[1:]
    parsed_questions = []

    for question in questions:
        parts = question.split('\n')
        q_text = parts[0]
        correct_answer = parts[1].split(": ")[1]

        parsed_questions.append((q_text, correct_answer))

    return parsed_questions

def Baseball_Quiz():
    questions = load_questions(r"BQ.txt")
    selected_questions = []
    
    while True:
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
        


def Baseball_Info():        
    df = pd.read_csv('BI.csv', header=None, encoding = 'utf-8')

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

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((" 1", 12346))
server_socket.listen(5)
print("서버가 시작되었습니다. 클라이언트를 기다립니다...")

while True:
    client_socket, addr = server_socket.accept()
    menu = ("다음과 같은 기능이 있습니다.\n4. 야구 퀴즈 5. 야구 정보 전달 6. 종료\n")
    client_socket.send(menu.encode())
    client_choice = client_socket.recv(1024).decode()
    if client_choice == '4':
        Baseball_Quiz()
    elif client_choice == "5":
        Baseball_Info()
    elif client_choice == "6":
        print("클라이언트와의 연결을 종료합니다.")
        client_socket.close()
        break
