# join.py

import streamlit as st
import sqlite3 as db
import pandas as pd

# join 
#  - 두 표에 나뉘어 있는 정보를 연결해서 
#    한번에 보여주는 기능

# # 1. 파일 읽기
# 데이터 = pd.read_csv("수강신청_100줄.csv") 

# # 2. db를 만들기
# db저장소 = db.connect("school.db")

# # 3. 저장소 저장
# # to_sql() 판다스 표를 DB에 저장
# 데이터.to_sql("수강신청",db저장소
#              ,if_exists="replace"
#              ,index=False)

# # 4.DB조작
# 마우스 = db저장소.cursor()
# st.title("join")

# # 5. 전체 조회
# # [(),()]
# 마우스.execute("""
#      select * from 수강신청
#     """)

# 전체 = 마우스.fetchall()

# # 6. 화면에 보이기
# 칸이름 = ["번호", "학번", "이름",
#         "전화번호", "학과", "과목명", "교수", "강의실"]

# 표 = pd.DataFrame(전체,columns=칸이름)
# st.write(f"전체 {len(전체)}줄")
# st.dataframe(표)

# 현재 테이블의 문제
# 1. 내용의 중복이 심하다
#  수강신청을 10번 하면 10번다 똑같은 학생정보
#  가 들어간다. 

# 컴공과  김민지가 핸드폰번호 010-1111-0011
# 2. select 위에서 부터 한줄 한줄 읽으면서
#   조건이 맞으면 수정한다 (성능 안! 좋아짐)

# 테이블을 쪼개자!
# 최대한 중복없이 테이블을 한 줄로 설명할수있게
# 나눠자

# 한줄 설명 - 학생정보 테이블
# 수강신청 테이블, 과목 테이블
# 저장 할때는 나누고 보여줄 때(화면) 이어서(join)
db저장소 = db.connect("school.db")


마우스 = db저장소.cursor()
st.title("join")

# 테이블 삭제

마우스.execute("drop table if exists students")
마우스.execute("drop table if exists courses")
마우스.execute("drop table if exists enrollments")

# 학생 정보
마우스.execute("""
    create table if not exists students(
    학번    text  primary key,
    이름    text  not null,
    전화번호 text  not null   unique,
    학과    text  not null
    )
""")

# 과목표 : 과목 하나 
마우스.execute("""
    create table if not exists courses(
        과목번호  integer  primary key  autoincrement,
        과목명    text     not null  unique,
        교수      text     not null,
        강의실    text     not null
    )
""")


# 수강 신청표 : 누가 무엇을 신청했나?
마우스.execute("""
    create table if not exists enrollments(
        신청번호  integer  primary key  autoincrement,
        학번      text     not null,
        과목번호  integer  not null
    )
""")

# 나누는 기준
# 1. 한줄 =?
#  같은 값이 반복된다.
#  하나를 고치려면 여러 줄을 고쳐야한다. 
#  정보를 지우면 다른 정보도 같이 사라진다. 
#  데이터를 넣을 떄 빈칸 (None) 생긴다.

# 2. 위에 기준 중 하나라도 보이면 나눈다!

# join 
# 데이터 저장 하기 
# 스트림릿이 실행할 때 마다 데이터가 추가된다
# 데이터가 두번이상 들어가지 않게 설정

# csv 파일을 읽을 때 테이블의 타입과 똑같아야된다.
# 그냥 csv파일을 읽으면 학번이 저장될 때 숫자로 저장될 
# 우려가 있다.

데이터 = pd.read_csv("수강신청_100줄.csv",
                    dtype={"학번" : str}) 

# 1. 학생 테이블 채우기
#  drop_duplicates 
# drop (버리다) + duplicates(중복들)
# 학번이 같으면 맨 처음 한 줄만 남기고 나머지는 버려라!
# subset=["학번"] 기준컬럼을 지정한다 

# DB에 저장
# to_sql(테이블명,DB명,if_exists=append)
#  append - 덧붙이다. 이미 만들어진 테이블에 데이터만 추가해라
#  

학생 = 데이터[["학번", "이름", "전화번호", "학과"]].drop_duplicates(subset=["학번"])
학생.to_sql("students", db저장소, if_exists="append", index=False)

# 2. 과목 테이블 채우기
# subset 안 쓴 이유는 데이터가 엉킨 줄이 없다
# 데이터를 구별할 이유가 없다#
# 학생 테이블은 동명이인이 각각 다른 학과!그래서 
# subset 기준을 나눈것

# 안전하게 작성하고 싶을 경우 
# 과목 = 데이터[["과목명", "교수", "강의실"]].drop_duplicates(subset=["과목명"])

과목 = 데이터[["과목명", "교수", "강의실"]].drop_duplicates()
과목.to_sql("courses", db저장소, if_exists="append", index=False)

# 3. 수강신청 테이블 채우기
#  -1) 과목 먼저 가져오기
마우스.execute("select 과목번호, 과목명 from courses")
과목번호표 = pd.DataFrame(마우스.fetchall(), columns=["과목번호", "과목명"])

#  -2) 과목명이 같은 줄끼리 붙여서 과목번호 얻기
신청 = 데이터.merge(과목번호표, on="과목명")

#  -3) 학번,과목번호만 남기고 중복 신청 지우기
신청 = 신청[["학번", "과목번호"]].drop_duplicates()
신청.to_sql("enrollments", db저장소, if_exists="append", index=False)

# 확정
db저장소.commit()
st.write(f"수강신청 {len(데이터)}줄 → 학생 {len(학생)}명 / 과목 {len(과목)}개 / 신청 {len(신청)}건")

마우스.execute(
    "SELECT 학번, 과목번호 FROM enrollments WHERE 학번 = 2401",
)

결과 = 마우스.fetchall()

for 학번, 과목번호 in 결과:
    st.write(f"{학번} {과목번호}")