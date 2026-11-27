# 4_친구목록.py
# 친구 목록 창을 띄우고 그 위에 검색하는 창
# 친구 목록 검색하는 sql명령어

import streamlit as st
import sqlite3 as db
from pathlib import Path

db저장소 = db.connect(Path(__file__).resolve().with_name("kakao.db"))
마우스 = db저장소.cursor()

# 친구목록에 필요한 테이블?
#  - members 테이블 활용해서 친구 검색
회원 = st.session_state.get("로그인한유저")

# 로그인 회원이 없으면 None 이 나옴
st.title("카카오 친구목록")

if 회원 is None:
    st.write("로그인 부터 하세요!")
    st.page_link("로그인.py",label="로그인하러 가기")

else:
   # 1. 준비 : 나는 누구?
   나 = 회원[0]  # 이름이 같은 다른 회원도 보이도록 회원번호로 구별한다.

   # 친구목록 검색창
   검색어 = st.text_input("이름으로 검색").strip()

   # 검색했을 때 나오는 친구만 가져오기
   # 조건은 나 빼고 나와야됨!
   # %검색어%  어디든 검색어 문자가 포함되어있으면

   # %강동원% (검색창은 이거를 많이쓴다)
   # 강동원 내일 영화 시사회 참석
   # 오늘 top 연예인 강동원 입니다.

   # 강동원%
   # 강동원으로 시작하는 문자만 검색해

   # %강동원
   # 강동원으로 끝나는 문자만 검색해

   마우스.execute("""
    select
        아이디,이름
    from
        members
    where
        회원번호 != ? and 이름 like ?
    order by
        이름, 아이디

    """, (나, f"%{검색어}%"))

   친구목록 = 마우스.fetchall()

   st.write("친구수", len(친구목록), "명")
   if not 친구목록:
       st.info("검색 결과가 없어요." if 검색어 else "아직 다른 회원이 없어요.")

   for  아이디, 이름 in 친구목록:
        with st.container(border=True):
            st.write(f"👤 **{이름}** :  **{아이디}**")



   # 2. 조회: 나만 빼고 모든 회원가져오기
#    마우스.execute(f"""
#       select
#         이름
#       from
#         members
#       where
#         이름 != '{나}'
#    """)

#    친구목록 = 마우스.fetchall()
#    # 3. 출력
#    #     친구수
#    st.write("친구수 ", len(친구목록),"명")

#    #    친구 목록
#    #    for문을 write()
#    for  이름 in 친구목록:
#         with st.container(border=True):
#             st.write(f"👤 **{이름[0]}**")

db저장소.close()

# 전체 친구목록
# 데이터를 보여줄때 페이지를 끊어서 보여준다
# 15개 ,5개씩 (페이지네이션)
