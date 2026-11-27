import streamlit as st
import sqlite3 as db
from pathlib import Path

db저장소 = db.connect(Path(__file__).resolve().with_name("kakao.db"))
마우스 = db저장소.cursor()

st.title("💛 카카오 로그인")

아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()

if st.button("로그인"):
    마우스.execute("""
        select * from members
        where 아이디 = ? and 비밀번호 = ?
    """, (아이디, 비밀번호))
    회원 = 마우스.fetchone()

    if 회원 == None:
        st.warning("아이디 또는 비밀번호를 확인해주세요")
    else:
        st.session_state["로그인한유저"] = 회원
        st.switch_page("채팅목록.py")

st.page_link("회원가입.py", label="아직 회원이 아니라면? 회원가입")

