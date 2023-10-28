import csv
from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = False

t="ddd"

while True:
    data=[]
    
    # CSV 파일을 읽기 모드로 열고 데이터 읽기
    with open('Baseball.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    # 데이터를 표로 출력
    # headers는 열 헤더를 나타냅니다. 필요에 따라 변경하세요.
    headers = data[0]  # 첫 번째 행을 열 헤더로 사용
    data = data[1:]  # 첫 번째 행을 제외한 나머지 데이터

    # "pretty" 포맷을 사용하여 표를 출력
    table = tabulate(data, headers, tablefmt="fancy_grid")
    print(table)
    t=input()
    
    
    
    
# 데이터 프레임 생성
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# 데이터 프레임을 표로 출력
table = tabulate(df, headers='keys', tablefmt='pretty', showindex=False)
print(table)

