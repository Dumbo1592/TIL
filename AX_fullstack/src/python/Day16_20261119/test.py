import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from itertools import combinations

Data = pd.read_csv(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\src\python\Day16_20261119\엘리베이터_회귀실습_수정.csv", encoding="utf-8-sig")

def fun(Data):
    least={}
    X_Data = Data.drop(columns=["대기시간(초)"]).columns
    model = LinearRegression()
    
    for i in range(len(X_Data)+1):
        for cols in combinations(X_Data,i+1):
            X,Y = Data[list(cols)], Data["대기시간(초)"]
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
            model.fit(X_train,Y_train)
            예측시간 = model.predict(X_test)
            MAE = mean_absolute_error(Y_test,예측시간)
            base = [Y_train.mean()] * len(Y_test)
            if not least:
                least["columns"] = X.columns.tolist()
                least["MAE"] = MAE
                st.write("columns: " , least["columns"], "MAE: ", least["MAE"])
                st.line_chart({"테스트": 예측시간, "기준선": base, "테스트_기준선": [MAE] * len(Y_test)})
            else:
                if least["MAE"] > MAE:
                    # 기준선_MAE = mean_absolute_error(Y_test,base)
                    least["columns"] = X.columns.tolist()
                    least["MAE"] = MAE
                    st.write("columns: " , least["columns"], "MAE: ", least["MAE"])
                    st.line_chart({"테스트": 예측시간, "기준선": base,"테스트_기준선": [MAE] * len(Y_test)})

    # X = Data[X_Data]
    # Y = Data["대기시간(초)"]
    # model.fit(X,Y)
    # print(X_Data)
    # print(model.coef_)

fun(Data)
     