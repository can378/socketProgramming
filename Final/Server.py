import socket
import select
from LookUp import LookUpPlayer,LookUpTeam
from SP import ScorePredictFunction
HOST = '192.168.16.196'
PORT = 1233
status="homeMenu"
    
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
                data = conn.recv(1024).decode('utf-8')
                print(f'클라이언트가 선택한 번호:{data}')
                message=""
                
                #잘못된 입력 처리
                try:
                    n = int(data)
                except ValueError:
                    #conn.sendall(f'입력값이 올바르지 않습니다:{data}\n'.encode('utf-8'))
                    message+="\n잘못된 입력값입니다. 다시 입력하세요\n"
                    conn.sendall(message.encode('utf-8'))
                    continue



                    
                if status=="homeMenu":
                    

                    #선택
                    if n == 1:
                        message+="\n2024경기 성적 예측입니다.\n"
                        message+=ScorePredictFunction()
                        message+=homeMenuExplain
                    elif n == 2:
                        message+="\n조회할 경기의 년도를 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                        status="lookUpTeam"
                        #LookUpTeam()
                        #conn.sendall("n==2".encode('utf-8'))
                    elif n == 3 :
                        message+="\n조회할 선수의 ??를 입력하세요.\n(전체 조회는 1을 입력하세요)\n"
                        status="lookUpPlayer"
                        #LookupPlayer()
                        #conn.sendall("n==3".encode('utf-8'))
                    elif n==4:
                        message+="야구퀴즈 선택\n"
                        status="quiz"
                        #conn.sendall("n==4".encode('utf-8'))
                    elif n==5:
                        message+="야구상식 선택\n"
                        status="info"
                        #conn.sendall("n==5".encode('utf-8'))
                    elif n==6:
                        # 클라이언트 접속 해제
                        conn.sendall(f"종료 선택\n".encode('utf-8'))
                        conn.close()
                        readsocks.remove(conn)  #readsocks에서 제거
                        
                    else : #conn.sendall(" ".encode('utf-8'))
                        message+="\n해당 숫자는 선택지에 없습니다.\n"
                        message+=homeMenuExplain
                        
                
                elif status=="lookUpPlayer":
                    if n==1: message+="선수 전체 조회를 선택"
                    else: message+=LookUpPlayer(n)
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="lookUpTeam":
                    if n==1: message+="경기 전체 조회를 선택"
                    else: message+=LookUpTeam(int(n))
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="quiz":
                    message+="야구 퀴즈"
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                    
                    
                elif status=="info":
                    message+="야구 정보"
                    
                    #다시 홈메뉴로
                    message+=homeMenuExplain
                    status="homeMenu"
                
                else: status="homeMenu"
                    

                conn.sendall(message.encode('utf-8'))
                


                    
