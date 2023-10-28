import pandas as pd
import csv
from tabulate import tabulate
tabulate.WIDE_CHARS_MODE = False

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


#pip install pandas
#pip install tabulate
#pip install tabulate[widechars] 


def LookupPlayer():
    df1=pd.read_csv("Baseball_copy.csv",encoding='UTF-8')

    #메뉴 선택
    choose=input("choose one\n1.all  2.name  3.role  4.poition  5.year  6.exit\n")
    
    if choose=='all':
        print("inquire all")
        
    elif choose=='name':
        name=input("Enter the name=")
        df1=df1.loc[df1["Name"]==name]
        
    elif choose=='role':
        role=input("Enter the role=")
        df1=df1.loc[df1["Role"]==role]
        
    elif choose=='position':
        position=input("Enter the position=")
        df1=df1.loc[df1["Position"]==position]
        
    elif choose=='year':
        year=input("Enter the year=")
        df1=df1.loc[df1["Year"]==year]
        
    elif choose=='exit': 
        print("exit")
        return 0
    else: print("wrong input. print all athletes")
    
    
    df1=pd.DataFrame(df1)
    table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
    print(table1)
    
    #변수가 테이블에 존재하지 않으면 예외처리




def LookUpTeam():
    df1=pd.read_csv("Baseball_Team.csv",encoding='UTF-8')

    #메뉴 선택
    choose=input("choose one\n1.all  2.year\n")
    
    if choose=='all':
        print("inquire all")
   
    elif choose=='year':
        year=input("Enter the year=")
        df1=df1.loc[df1["Team_Year"]==year]
        
    elif choose=='exit': 
        print("exit") 
        return 0
    else: print("wrong input. print all athletes")
    
    
    df1=pd.DataFrame(df1)
    table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
    print(table1)
    
    #변수가 테이블에 존재하지 않으면 예외처리





while True:
    
    menu=input("숫자를 선택해 주세요.\n1.팀 성적 조회  2.선수 조회\n")
    
    if menu=="1":    LookUpTeam()
    elif menu=="2":  LookupPlayer()
    else:print("잘못된 입력입니다.")
    


    t=input("다시 조회[Y/N]")
    if t!="y"and t!="Y": break
    
    
    
    
    
'''
print(df1.columns)
print(df1.rename(columns={"Player_Name":"이름"},inplace=False))#명칭 바꿔서 출력 inplace는 적용 여부
df1.sort_values(by="AVG",ascending=True)
print(df1[["Player_Name","Position"]])
print(df1.loc[df1["Player_Name"]=="고우석"])
print(df1.loc[df1["Role"]=="투수"])
'''

'''
data=[]

# CSV 파일을 읽기 모드로 열고 데이터 읽기
with open('Baseball.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(row)



headers = data[0]  # 첫 번째 행을 열 헤더로 사용
data = data[1:]  # 첫 번째 행을 제외한 나머지 데이터

# 표를 출력
table = tabulate(data, headers, tablefmt="fancy_grid")
print(table)
'''
    
    
    
    
