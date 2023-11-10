import pandas as pd
import csv
from tabulate import tabulate
tabulate.WIDE_CHARS_MODE = False

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


#pip install pandas
#pip install tabulate
#pip install tabulate[widechars] 



def LookUpPlayer(choose):
   
    df1=pd.read_csv("Baseball_Player.csv",encoding='UTF-8')
    wrong=False
    

    if str(choose)=="1":
        print("모두 출력")
    else:
        df1=df1.loc[df1["Name"]==choose]
    
    

    if df1.empty: return "\n잘못된 입력값이거나 해당 선수의 데이터가 없습니다."
    else:
        df1=pd.DataFrame(df1)
        table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
        return table1




def LookUpTeam(input):

    df1=pd.read_csv("Baseball_Team.csv",encoding='UTF-8')

    
    #잘못된 입력 처리
    try:
        choose = int(input)
    except ValueError:
        return"\n잘못된 입력값입니다.\n"
                
                
    if choose==1:
        df1=df1.loc[df1["Ranking"]!=0]
    else:
        df1=df1.loc[df1["Team_Year"]==choose]
    
    
    if df1.empty : return "\n잘못된 입력값이거나 해당 년도의 경기 데이터가 없습니다."
    else:
        df1=pd.DataFrame(df1)
        table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
        return table1



'''
def LookupPlayer_original():
    
    
    while True:
        df1=pd.read_csv("Baseball_Player.csv",encoding='UTF-8')
        wrong=False
        
        #메뉴 선택
        print("=========================================================")
        choose=input("choose one\n1.all  2.name  3.role  4.poition  5.year  6.exit\n")
        
        
        if choose=='all'or choose=="1":
            print("모두 출력")
            
        elif choose=='name'or choose=="2":
            name=input("Enter the name=")
            df1=df1.loc[df1["Name"]==name]
            
        elif choose=='role'or choose=="3":
            role=input("Enter the role=")
            df1=df1.loc[df1["Role"]==role]
            
        elif choose=='position'or choose=="4":
            position=input("Enter the position=")
            df1=df1.loc[df1["Position"]==position]
            
        elif choose=='year'or choose=="5":
            year=input("Enter the year=")
            df1=df1.loc[df1["Year"]==int(year)]
            
        elif choose=='exit'or choose=="6": 
            return 0
        else: 
            print("wrong input")
            wrong=True
        
        
        if wrong==False : 
            if df1.empty: print("wrong input")
            else:
                df1=pd.DataFrame(df1)
                table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
                print(table1)
'''
'''
def LookUpTeam_original():
    
    
    while True:
        df1=pd.read_csv("Baseball_Team.csv",encoding='UTF-8')
        wrong=False
        
        #메뉴 선택
        print("=========================================================")
        choose=input("choose one\n1.all  2.year  3.exit\n")
        
        if choose=='all'or choose=="1":
            df1=df1.loc[df1["Ranking"]!=0]
            
        elif choose=='year'or choose=="2":
            year=input("Enter the year=")
            df1=df1.loc[df1["Team_Year"]==int(year)]
            
        elif choose=='exit'or choose=="3": 
            return 0
        
        else: 
            print("wrong input") 
            wrong=True
        
        
        if wrong==False :
            if df1.empty : print("wrong input")
            else:
                df1=pd.DataFrame(df1)
                table1 = tabulate(df1, headers='keys', tablefmt='fancy_grid', showindex=False)   
                print(table1)
'''
        
        


'''
while True:
    print("=========================================================")
    menu=input("숫자를 선택해 주세요.\n1.팀 성적 조회  2.선수 조회  3.종료 \n")
    
    if menu=="1":    LookUpTeam()
    elif menu=="2":  LookupPlayer()
    elif menu=="3": break
    else:print("잘못된 입력입니다.")
    
'''
    
    
    
    
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
    
    
    
    
