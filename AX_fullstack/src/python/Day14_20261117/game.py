import pandas as pd
import time
import streamlit as st

# x = 내가 알고 있는 것!
# y = 알고 싶은 것!

# 스트림릿 10초 세기 5번

목표 = 10 # 맞출 시간
횟수 = 5 # 한 라운드에 시도하는 횟수!

st.title("눈 감고 10초 맞추기")
st.caption(f"시작을 누르고, {목표}초가 지났다고 느껴지면 멈춤을 누름")

if st.button("연습: 10초가 어떤 느낌인지 보기"):
    자리 = st.empty()
    