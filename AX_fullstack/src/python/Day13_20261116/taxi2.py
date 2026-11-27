import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.subheader("규칙")
st.write("1km 늘 때 마다 얼마씩?")
st.write(" 1km - 2000원")
st.write(" 2km - 4000원")
st.write(" 3km - 6000원")
st.write("요금 = 거리 x 2000")



기본요금 = 4800
KM_요금 = 1000
거리 = st.number_input("거리:",value=1)
요금 = 거리 * KM_요금

st.subheader("택시 요금 그래프")
거리 = st.slider("몇 km 까지 볼까요?",1,10,5)

표 = pd.DataFrame({
    "거리" : list(range(0,거리+1))
})

# st.write(표["거리"])

표["기본요금있음"] = 표["거리"] * KM_요금 + 기본요금
표["기본요금없음"] = 표["거리"] * KM_요금

st.line_chart(표,x="거리", y=["기본요금있음","기본요금없음"])
