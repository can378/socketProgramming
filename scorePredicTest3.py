import pandas as pd
from sklearn.linear_model import LinearRegression

# 데이터 가져오기
data = pd.read_csv("Baseball_Team.csv")


# 입출력 변수 설정
x_train = data[['Team_Year','Win_Percentage', 'Ranking', 'Score_get', 'Score_Lost']]#입력 변수
y_train = data[['Team_Year','Win_Percentage', 'Ranking', 'Score_get', 'Score_Lost']]#출력 변수

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(x_train, y_train)

# 2024년 데이터 예측
predictions_2024 = model.predict(data[['Team_Year','Win_Percentage', 'Ranking', 'Score_get','Score_Lost']])
Team_Year_2024,win_percentage_2024, ranking_2024, score_get_2024, score_lost_2024 = predictions_2024[0]

print(Team_Year_2024)
print(f"2024년 예상 Win_Percentage: {win_percentage_2024}")
print(f"2024년 예상 Ranking: {ranking_2024}")
print(f"2024년 예상 Score_Get: {score_get_2024}")
print(f"2024년 예상 Score_Lost: {score_lost_2024}")
