import socket
import select
import random
from LookUp import LookupPlayer,LookUpTeam

HOST = '172.30.1.63'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST, PORT))
    s.listen()
    print('서버 시작')

    readsocks = [s]

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
                message="숫자 선택\n1.성적 예측  2.경기 성적 조회  3.선수 조회  4.? 5.? 6.종료"
                conn.send(message.encode())
                
                data = conn.recv(1024).decode('utf-8')
                print(f'클라이언트가 선택한 번호:{data}')

                
                #잘못된 입력 처리
                try:
                    n = int(data)
                except ValueError:
                    conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                    continue

                
                
                if n == 1:
                    conn.sendall("n==1".encode('utf-8'))
                elif n == 2:
                    LookUpTeam()
                    conn.sendall("n==2".encode('utf-8'))
                elif n ==3 :
                    LookupPlayer()
                    conn.sendall("n==3".encode('utf-8'))
                elif n==4:
                    conn.sendall("n==4".encode('utf-8'))
                elif n==5:
                    conn.sendall("n==5".encode('utf-8'))
                elif n==6:
                    # 클라이언트 접속 해제
                    conn.sendall(f"종료".encode('utf-8'))
                    conn.close()
                    readsocks.remove(conn)  #readsocks에서 제거
                else : conn.sendall(" ".encode('utf-8'))

                    
