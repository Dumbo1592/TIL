import pandas as pd

# df = pd.DataFrame({
#     "집계_기준": ["출발시간", "도착시간", "출발시간",
#                  "출발시간", "도착시간", "출발시간"],
#     "기준_시간대": [800, 805, 825, 900, 905, 930],
#     "대여소": ["A", "B", "B", "A", "C", "C"],
#     "전체_건수": [30, 20, 45, 15, 25, 40]
# })

# 출발시간 = df[df["집계_기준"]=="출발시간"].copy()
# # print(출발시간)
# df["시"] = df["기준_시간대"]//100
# 합계 = df.groupby("시")["전체_건수"].sum()
# print(합계)
# print(df.sort_values(by="전체_건수", ascending=False))

# import pandas as pd

# df = pd.DataFrame({
#     "대여소": ["A", "B", "A", "C", "B", "C", "A", "B"],
#     "집계_기준": ["출발", "출발", "도착", "출발",
#                  "출발", "도착", "출발", "도착"],
#     "이용건수": [30, 50, 20, 40, 25, 15, 35, 10]
# })

# 출발 = df[df["집계_기준"]=="출발"]
# 합계 = 출발.groupby("대여소")["이용건수"].sum()
# 합계 = 합계.sort_values(ascending=False)
# print(합계.head(2))

# import pandas as pd

# df = pd.DataFrame({
#     "대여소": ["A", "B", "A", "C", "B", "C"],
#     "이용건수": [2, 3, 4, 2, 1, 3],
#     "전체_이용_분": [40, None, 80, 50, None, 60]
# })

# # print(df.isna().sum())
# 유효 = df[df["전체_이용_분"].notna()]
# 이용건수 = 유효["이용건수"].sum()
# 전체이용분 = 유효["전체_이용_분"].sum()
# print(이용건수)
# print(전체이용분)
# print(round((전체이용분/이용건수),2))

# import pandas as pd

# df = pd.DataFrame({
#     "대여소": ["A", "B", "C", "A", "B", "D", "A", "B"],
#     "집계_기준": ["출발", "출발", "출발", "도착",
#                  "도착", "도착", "출발", "도착"],
#     "이용건수": [30, 50, 20, 40, 25, 35, 10, 15]
# })

# 출발 = df[df["집계_기준"] == "출발"]
# 도착 = df[df["집계_기준"] == "도착"]

# 나간 = 출발.groupby("대여소")["이용건수"].sum()
# 들어온 = 도착.groupby("대여소")["이용건수"].sum()

# 순유입 = 들어온 - 나간
# print(나간)

# 순유입 = 들어온.sub(나간, fill_value=0)

# print(순유입)

import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "대여소": ["A", "B", "C", "A", "B", "C"],
    "이용건수": [30, 50, 20, 40, 25, 60]
})

전체이용건수 = df["이용건수"].sum()
합계 = df.groupby("대여소")["이용건수"].sum()

st.title("따릉이 이용 현황")
st.metric("따릉이 이용 현황", 전체이용건수, delta=None)
st.bar_chart(합계)
