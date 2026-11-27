import streamlit as st

st.title("단어 퀴즈")

#3 퀴즈 1
st.header("문제 1")
st.write("사람이 정한 규칙에 따라 작동하는 AI는?")

#정답 입력 받기
정답1 = st.text_input("정답 입력", key = "answer1")

if 정답1 == "규칙 기반 ai":
    st.success("정답") 
elif 정답1: st.error("오답")

#4 퀴즈 2
st.header("문제 2")
st.write("데이터에서 패턴을 학습하는 기술?")

#정답 입력 받기
정답2 = st.text_input("정답 입력", key = "answer2")

if 정답2 == "머신러닝":
    st.success("정답") 
elif 정답2: st.error("오답")

#"" false
#"한문자" true
#python -m streamlit run app.py
