import socket
import select

import random
import pandas as pd

from LookUp import LookUpPlayer,LookUpTeam
from InfoAndQuiz import Baseball_Quiz
from SP import ScorePredictFunction

HOST = '172.30.1.61'
PORT = 1233




def Baseball_Info(request):        
   
    df = pd.read_csv('Final/BI.csv', header=None, encoding = 'utf-8')
    message="\n"
    
    
    if int(request) == 1:
        column_data = df.iloc[1:2, 0]
        for row in column_data:
            message+=(row + '\n')
            
    if int(request) == 2:
        column_data = df.iloc[1:2, 1]
        for row in column_data:
            message+=(row + '\n')
            
    if int(request) == 3:
        column_data = df.iloc[1:2, 2]
        for row in column_data:
            message+=(row + '\n')
            
            
    return message




    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    
    s.bind((HOST, PORT))
    s.listen()
    print('서버 시작')

    readsocks = [s]

    homeMenuExplain="\n\n==== 원하는 숫자를 선택하세요.\n==== 1.성적예측  2.경기조회  3.선수조회  4.야구퀴즈  5.야구상식  6.종료\n"
    status="homeMenu"
    
    
    
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
                data = conn.recv(1024).decode('utf-8')
                print(f'클라이언트가 선택한 번호:{data}')
                message=""
                
                
                
                
                n=data
                '''
                if status!="lookUpPlayer" or status!="quiz":
                    #잘못된 입력 처리
                        try:
                            n = int(data)
                        except ValueError:
                            #conn.sendall(f'입력값이 올바르지 않습니다:{data}\n'.encode('utf-8'))
                            message+="\n잘못된 입력값입니다. 다시 입력하세요\n"
                            conn.sendall(message.encode('utf-8'))
                            continue
                else:n=data
                '''




                if status=="homeMenu":
                    n=int(data)
                    
                    #선택
                    if n == 1:
                        message+="\n2024경기 성적 예측입니다.\n"
                        message+=ScorePredictFunction()
                        message+=homeMenuExplain
                        
                    elif n == 2:
                        message+="\n조회할 경기의 년도를 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                        status="lookUpTeam"
                        
                        
                    elif n == 3 :
                        message+="\n조회할 선수의 이름을 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                        status="lookUpPlayer"
                        
                        
                    elif n==4:
                        message+="야구퀴즈 선택\n"
                        status="quiz"
                        
                    elif n==5:
                        message+="\n원하는 정보를 선택하세요.\n1.역사  2.지표  3.경기방식과 기본 규칙\n"
                        status="info"
                        
                    elif n==6:
                        # 클라이언트 접속 해제
                        conn.sendall(f"종료 선택\n".encode('utf-8'))
                        conn.close()
                        readsocks.remove(conn)  #readsocks에서 제거
                        
                    else :
                        message+="\n해당 숫자는 선택지에 없습니다.\n"
                        message+=homeMenuExplain
                        
                
                elif status=="lookUpPlayer":
                    
                    message+=LookUpPlayer(data)
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="lookUpTeam":
                    
                    message+=LookUpTeam(int(data))
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="quiz":
                    message+="야구 퀴즈"
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="info":
                    
                    message+=Baseball_Info(int(data))
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                
                else: 
                    message+="잘못된 상태"
                    status="homeMenu"
                    

                conn.sendall(message.encode('utf-8'))
                


                    
