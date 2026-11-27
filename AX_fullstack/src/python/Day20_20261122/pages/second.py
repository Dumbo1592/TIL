# second.py
import streamlit as st

st.title("2번 페이지")
st.page_link("pagelink.py", 
             label="1번 페이지로 가기",)

로그인아이디 = "eryna"

# 세션에서 꺼내기
st.write(st.session_state["로그인아이디"])
st.write(st.session_state["이름"])
