# pagelink.py
# 모든 서비스의 기본 기능 4가지
# - CRUD
# Create
# Read
# Update
# Delete

# 페이지 이동
# - 페이지 + 연결
# 누르면 다른 페이지로 가는 링크

import streamlit as st

st.title("1번 페이지")
# page_link("페이지경로")
# 현재 실행중인 pagelink.py 위치를 기준으로 경로를 찾는다
# 로그인아이디 변수는 현재 파일에서만 사용이 가능하다, 다른 페이지로 이동이 불가능하다

# session
# - 내가 사이트에 들어와있는 동안 나를 기억해주는 것
# - 사이트들끼리 정보를 공유할 수 있다.

# session_state[key(이름표)]
# - session(접속해 있는 동안) + state(상태)
# - 페이지를 이동해도 지워지지 않는 상자(딕셔너리)
# - key와 value 이루어져있다.

st.page_link("pages/second.py", 
             label="2번 페이지로 가기",)

로그인아이디 = "eryna"

# 세션 저장
st.session_state["로그인아이디"] = "eryna"
st.session_state["이름"] = "이서희"

st.write(로그인아이디)