import pandas as pd
from sklearn.linear_model import LinearRegression
# ── AI 설명·수정 ──
# 10줄 💬 R²를 쓰려면 여기에 r2_score를 함께 import해야 합니다.
# 51줄 💬 테스트 데이터 예측값입니다. 이 값과 정답(Y_test)을 비교해 R²를 구합니다.
# 53줄 💬 이 아래에 R2 = r2_score(Y_test, 예측점수) 한 줄을 추가하면 예측률을 구할 수 있습니다.
# 54줄 💬 출력에 R2도 넣으세요. 0.85면 정답 변동의 약 85%를 설명한다는 뜻입니다.
# 55줄 💬 CSV만 읽고 fun을 호출하지 않아 아무 결과도 나오지 않습니다. 아래에 fun(...) 호출이 필요합니다.
# ──────────────
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

# df = pd.DataFrame({
#     "주행거리": [10000, 20000, 30000, 40000, 50000, 60000],
#     "연식": [2023, 2022, 2021, 2020, 2019, 2018],
#     "사고횟수": [0, 1, 0, 2, 1, 3],
#     "가격": [2800, 2500, 2400, 2000, 1900, 1500]
# })

# X = df[["주행거리","연식","사고횟수"]]
# Y = df["가격"]

# model = LinearRegression()
# model.fit(X,Y)
# df["예측가격"] = model.predict(X)

# MAE = mean_absolute_error(df["가격"], df["예측가격"])

# 가격 = df[model.predict({
#     "주행거리" : [35000],
#     "연식" : [2021],
#     "사고횟수" : [1]
# })]

# Data = pd.read_csv(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\캐릭터_스탯.csv")

# 입력 = ["STR","DEX","CON"]

# X_train, X_test, Y_train, Y_test = train_test_split(Data[입력], Data["전투력"], test_size = 0.2, random_state = 1)

# model = LinearRegression()
# model.fit(X_train, Y_train)

# for 이름, w in zip(입력, model.coef_):
#     print(이름,"1 올리면 전투력: ",round(w,1),"증가")

def fun(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)
    model = LinearRegression()
    model.fit(X_train,Y_train)
    예측점수 = model.predict(X_test)
    MSE = mean_squared_error(Y_test, 예측점수)
    MAE = mean_absolute_error(Y_test, 예측점수)
    print(f"MSE:{MSE} MAE:{MAE}")
    for 이름, w in zip(X, model.coef_):
        print(이름,"1 올리면 전투력: ",round(w,2),"증가")
    
scoreData = pd.read_csv(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\시험점수.csv")

fun(scoreData[["공부시간"]], scoreData["점수"])
fun(scoreData[["공부시간","수면시간"]], scoreData["점수"])
fun(scoreData[["공부시간","수면시간","좋아하는숫자"]], scoreData["점수"])



