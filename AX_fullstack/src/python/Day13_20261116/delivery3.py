import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.DataFrame({
    "공부시간": [1, 2, 3, 4, 5, 6],
    "시험점수": [50, 58, 63, 72, 78, 85]
})

X = df[["공부시간"]]
Y = df["시험점수"]

model = LinearRegression()

model.fit(X,Y)

df["예측점수"] = model.predict(X)
MAE = mean_absolute_error(df["시험점수"], df["예측점수"])
