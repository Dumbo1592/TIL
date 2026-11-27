import sqlite3 as db
import streamlit as st

con = db.connect("검색어.db")
# 파일이 존재하면 기존 파일에 연결
# 파일이 없으면 새로 생성
# 기본적으로 현재 작업 폴더에 생성

조작 = con.cursor()
# 커서는 sql 명령을 실행하고 결과를 가져오는 객체

조작.execute("""
    CREATE TABLE if not exists searchlist(
        msg TEXT
    )
""")
# 검색어.db 라는 파일 안에 searchlist라는 표를 만듦.

st.title("검색어 저장하는 DB보기")
검색어 = st.text_input("검색어").strip()

# 사용자가 문자열을 입력하는 입력창을 만듦

if st.button("검색"):
    # 조작.execute(
    #     "INSERT INTO searchlist VALUES (?)",
    #     (검색어,)
    # )
    조작.executescript(f"""
        INSERT INTO searchlist VALUES ('{검색어}')
    """)
    # INSERT INTO	테이블에 새로운 데이터를 추가하라는 명령
    # searchlist	데이터를 추가할 테이블 이름
    # VALUES	추가할 데이터의 값을 지정
    # '{검색어}'	검색어 변수에 저장된 문자열 값
    con.commit()
    st.success(f"{검색어} 저장 완료!")

con.close()