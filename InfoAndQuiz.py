import random
import pandas as pd



def load_questions():
    
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



#안쓰고 있음
def Baseball_Quiz():
    
    questions = load_questions()
    selected_questions = [] #퀴즈 질문들을 배열로 저장
    
    
    correct_count = 0

    if len(selected_questions) == 0:
        selected_questions = random.sample(questions, 10)

    for question, correct_answer in selected_questions:
        
        #client_socket.send(question.encode())
        #question을 보낸다.
        
        #client_answer = client_socket.recv(1024).decode()
        #answer을 받아온다.
        client_answer=""
        
        
        if client_answer.lower() == correct_answer.lower():
            correct_count += 1
            response = "정답입니다!"
        else:
            response = f"틀렸습니다. 정답은 '{correct_answer}'입니다."

        #client_socket.send(response.encode())
        #respond 전송
        

    # 맞춘 개수에 따른 메시지 전송
    if correct_count == 10:
        result_message = "모두 맞추셨습니다. 축하합니다!"
    elif correct_count >= 7:
        result_message = "7개 이상 맞추셨습니다. 잘 하셨어요!"
    elif correct_count >= 3:
        result_message = "3개 이상 맞추셨습니다. 더 분발하세요!"
    else:
        result_message = "하나도 못 맞추셨습니다. 계속 노력하세요!"
    
    return result_message

        
        


def Baseball_Info(input):        
   
    df = pd.read_csv('BI.csv', header=None, encoding = 'utf-8')
    message="\n"
    
    
    #잘못된 입력 처리
    try:
        request = int(input)
    except ValueError:
        return"\n잘못된 입력값입니다.\n"
    
    
    if request == 3:
        column_data = df.iloc[1:2, 2]
        for row in column_data:
            message+=(row + '\n')
            
    elif request == 1:
        column_data = df.iloc[1:2, 0]
        for row in column_data:
            message+=(row + '\n')
            
    elif request == 2:
        column_data = df.iloc[1:2, 1]
        for row in column_data:
            message+=(row + '\n')
    else:
        message+="\n해당되는 번호가 없습니다.\n"
            
    return message


        
