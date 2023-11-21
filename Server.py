import socket
import select

import random
import pandas as pd

from LookUp import LookUpPlayer,LookUpTeam
from InfoAndQuiz import Baseball_Info,load_questions
from SP import ScorePredictFunction

HOST = '1'
PORT = 9999


    
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
                #print(f'클라이언트 접속:{addr}')
                print("클라이언트 접속")
                readsocks.append(newsock)

                
            # 기존 클라이언트의 요청=============================================
            else:  
                
                conn = sock
                data = conn.recv(1024).decode('utf-8')
                message=""
                
                

                #잘못된 입력 처리
                try:
                    service_code_byte = bytes([int(data[0])])
                    n = int.from_bytes(service_code_byte, byteorder='big')
                except ValueError:
                    message="\n잘못된 입력값입니다.\n"
                    conn.sendall(message.encode('utf-8'))
                    continue




                #선택
                if n == 1:
                    message+="\n2024경기 성적 예측입니다.\n"
                    message+=ScorePredictFunction()
                    message+=homeMenuExplain
                    
                elif n == 2:
                    message+="\n조회할 경기의 년도를 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                    conn.send(message.encode())
                    
                    data = conn.recv(1024).decode('utf-8')
                    message=LookUpTeam(data)
                    message+=homeMenuExplain

                    
                elif n == 3 :
                    message+="\n조회할 선수의 이름을 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                    conn.send(message.encode())
                    
                    data = conn.recv(1024).decode('utf-8')
                    message=LookUpPlayer(data)
                    message+=homeMenuExplain

                elif n==4:
                    
                    question = load_questions()
                    
                    selected_question = random.choice(question)
                        
                    #question을 보낸다.
                    conn.send(selected_question[0].encode())
                        
                    #answer을 받아온다.
                    client_answer = conn.recv(1024).decode()
                        
                    if client_answer.lower() == selected_question[1].lower():
                        response = "정답입니다!\n"
                    else:
                        response = f"틀렸습니다. 정답은 '{selected_question[1]}'입니다.\n"

                    message+=response+"\n"
                    message+=homeMenuExplain
                        

                elif n==5:
                    message+="\n원하는 정보를 선택하세요.\n1.역사  2.지표  3.경기방식과 기본 규칙\n"
                    conn.send(message.encode())
                    
                    data = conn.recv(1024).decode('utf-8')
                    message=Baseball_Info(data)
                    message+=homeMenuExplain
                    
                elif n==6:
                    # 클라이언트 접속 해제
                    message="\n종료합니다.\n"

                else :
                    message+="\n해당 숫자는 선택지에 없습니다.\n"
                    message+=homeMenuExplain
                    


                conn.sendall(message.encode('utf-8'))
                
                if n==6:
                    conn.close()
                    readsocks.remove(conn)  #readsocks에서 제거
                    
                


                    
