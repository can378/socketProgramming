import pandas as pd
from sklearn.linear_model import LinearRegression


# 데이터 가져오기
data = pd.read_csv("Baseball_Team.csv")
data_2024 = pd.DataFrame(columns=['Team_Year', 'Win_Percentage', 'Ranking', 'Score_get', 'Score_Lost'])
data_2024[['Team_Year']]=2024



# 입출력 변수 설정
X = data[['Team_Year']]#분류기준
y = data[['Team_Year','Win_Percentage', 'Ranking', 'Score_get', 'Score_Lost']]#출력 변수

x_train=X[X['Team_Year'] < 2024]
y_train=y[y['Team_Year'] < 2024]

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(x_train, y_train)

# 2024년 데이터 예측
predictions_2024 = model.predict(data_2024[['Team_Year']])
Team_Year_2024,win_percentage_2024, ranking_2024, score_get_2024, score_lost_2024 = predictions_2024[0]


print("%.0f"%Team_Year_2024)
print("2024년 예상 Win_Percentage: %.3f"%win_percentage_2024)
print("2024년 예상 Ranking: %.0f" %ranking_2024)
print("2024년 예상 Score_Get: %.0f"%score_get_2024)
print("2024년 예상 Score_Lost: %.0f"%score_lost_2024)
