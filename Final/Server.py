import socket
import select

import random
import pandas as pd

from LookUp import LookUpPlayer,LookUpTeam
from InfoAndQuiz import Baseball_Info,load_questions
from SP import ScorePredictFunction

HOST = ' 1'
PORT = 1233




    


    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    
    s.bind((HOST, PORT))
    s.listen()
    print('서버 시작')

    readsocks = [s]

    homeMenuExplain="\n\n==== 원하는 숫자를 선택하세요.\n==== 1.성적예측  2.경기조회  3.선수조회  4.야구퀴즈  5.야구상식  6.종료\n"

    
    
    while True:
        readables, writeables, excpetions = select.select(readsocks, [], [])
        for sock in readables:
            
            # 신규 클라이언트 접속===============================================
            if sock == s:  
                newsock, addr = s.accept()
                print(f'클라이언트 접속:{addr}')
                readsocks.append(newsock)

                
            # 기존 클라이언트의 요청=============================================
            else:  
                
                conn = sock
                function_data = conn.recv(1)
                message=""
                
                

                #잘못된 입력 처리
                try:
                    n = int(function_data)
                except ValueError:
                    message="\n잘못된 입력값입니다. 다시 입력하세요\n"
                    conn.sendall(message.encode('utf-8'))
                    conn.recv(1024)
                    continue




                #선택
                if n == 1:
                    message+="\n2024경기 성적 예측입니다.\n"
                    message+=ScorePredictFunction()
                    message+=homeMenuExplain
                    
                elif n == 2:
                    message+="\n조회할 경기의 년도를 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                    conn.send(message.encode())
                    
                    Year_data = conn.recv(1024).decode('utf-8')
                    message=LookUpTeam(Year_data)
                    message+=homeMenuExplain

                    
                elif n == 3 :
                    message+="\n조회할 선수의 이름을 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                    conn.send(message.encode())
                    
                    Name_data = conn.recv(1024).decode('utf-8')
                    message=LookUpPlayer(Name_data)
                    message+=homeMenuExplain

                elif n==4:
                    
                    questions = load_questions()
                    selected_questions = [] #퀴즈 질문들을 배열로 저장
                    
                    
                    correct_count = 0

                    if len(selected_questions) == 0:
                        selected_questions = random.sample(questions, 10)

                    for question, correct_answer in selected_questions:
                        
                        #question을 보낸다.
                        conn.send(question.encode())
                        
                        #answer을 받아온다.
                        client_answer = conn.recv(1024).decode()
                        
                        
                        if client_answer.lower() == correct_answer.lower():
                            correct_count += 1
                            response = "정답입니다!\n\n"
                        else:
                            response = f"틀렸습니다. 정답은 '{correct_answer}'입니다.\n\n"

                        conn.send(response.encode())
                    
                    
                    # 맞춘 개수에 따른 메시지 전송
                    result_message=str(correct_count)+"개 맞췄습니다.\n"
                    
                    if correct_count == 10:
                        result_message += "모두 맞추셨습니다. 축하합니다!"
                    elif correct_count >= 7:
                        result_message += "잘 하셨어요!"
                    elif correct_count >= 1:
                        result_message += "더 분발하세요!"
                    else:
                        result_message += "하나도 못 맞추셨습니다. 계속 노력하세요!"
    
                    message+=result_message+"\n"
                    
                    message+=homeMenuExplain


                        

                elif n==5:
                    message+="\n원하는 정보를 선택하세요.\n1.역사  2.지표  3.경기방식과 기본 규칙\n"
                    conn.send(message.encode())
                    
                    Info_data = conn.recv(1024).decode('utf-8')
                    message=Baseball_Info(Info_data)
                    message+=homeMenuExplain
                    
                elif n==6:
                    # 클라이언트 접속 해제
                    conn.sendall(f"종료합니다.\n".encode('utf-8'))
                    conn.close()
                    readsocks.remove(conn)  #readsocks에서 제거
                    
                else :
                    message+="\n해당 숫자는 선택지에 없습니다.\n"
                    message+=homeMenuExplain
                    


                conn.sendall(message.encode('utf-8'))
                


                    
