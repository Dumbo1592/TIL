#main.py
# 항상 스트림릿은 main파일에서 실행!
# streamlit run main.py
import streamlit as st
import sqlite3 as db
from pathlib import Path

db저장소 = db.connect(Path(__file__).resolve().with_name("kakao.db"))
마우스 = db저장소.cursor()

마우스.execute("""
    create table if not exists members(
        회원번호   integer  primary key  autoincrement,
        아이디     text     not null  unique,
        비밀번호   text     not null,
        이름       text     not null,
        전화번호   text     not null  unique
    )
""")

# 웹페이지끼리 정보 공유하는 세션!
# 세션 칸 만들기

if "로그인한유저" not in st.session_state:
    st.session_state["로그인한유저"] = None


db저장소.close()

페이지 = st.navigation([
    st.Page("로그인.py", title="로그인", default=True),
    st.Page("회원가입.py", title="회원가입"),
    st.Page("채팅목록.py", title="채팅목록"),
    st.Page("채팅방.py", title="채팅방"),
    st.Page("친구목록.py", title="친구목록"),
])
페이지.run()
