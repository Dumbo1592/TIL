#3_채팅방.py
import streamlit as st
import sqlite3 as db
from pathlib import Path

db저장소 = db.connect(Path(__file__).resolve().with_name("kakao.db"))
마우스 = db저장소.cursor()

# 새로운 메시지를 저장하는 테이블

마우스.execute("""
    create table if not exists msg(
        메시지번호  integer  primary key  autoincrement,
        채팅방      text     not null,
        보낸사람    text     not null,
        내용        text     not null  check(length(trim(내용)) > 0),
        보낸시간    text     default (datetime('now', 'localtime')),
        수정됨      integer  default 0  check(수정됨 in (0, 1))
    )
""")

# default
# - 만약 데이터가 안 들어오면 기본값으로 칸을 채운다.
# - length(trim(내용)) > 0
#   trim : 앞 뒤 공백 제거!
#   length : 글자의 길이
#   테이블이 글자가 없으면 자체적으로 데이터를 안받음
# - 알아서 빈 칸 채우기!

# check
# - DB가 자체적으로 검사한다.
# - 이상한 값 막을려고함
# - check(수정됨 in (0, 1))
#   수정 됬다, 안됬다만 저장하기 위해서 check를 이용해서
#  0 , 1  빼고는 다른 숫자는 못 들어가게 막은것!

# datetime
# - 날짜와 시간 저장하는 타입

#1. 로그인 했나? 확인
#  로그인 되어있다면 채팅방 메시지를 가져오기
#        안 되어있다면 로그인 페이지로 이동해라!
회원 = st.session_state.get("로그인한유저")

# 로그인 회원이 없으면 None 이 나옴
if 회원 == None:
    st.title("카카오 채팅방")
    st.write("로그인 부터 하세요!")
    st.page_link("로그인.py",label="로그인하러 가기")

else:
    # 로그인 회원정보 있다!
    st.write(회원)
    # 2.준비
    #  나는 누구? 어느방?
    나 = 회원[1]  # 아이디 가져오기

    # 채팅방이름 세션에서 꺼내기
    채팅방이름 = st.session_state.get("채팅방")
    if not 채팅방이름:
        st.info("채팅목록에서 채팅방을 선택하세요.")
        st.page_link("채팅목록.py", label="채팅목록으로 가기")
        st.stop()
    st.title(채팅방이름)

    st.page_link("채팅목록.py"
                 ,label="뒤로가기(채팅목록)")


    # 3.조회
    마우스.execute("""
        select
           메시지번호, 보낸사람,내용,보낸시간
        from
            msg
        where
            채팅방 = ?
    """, (채팅방이름,))

    메시지목록 = 마우스.fetchall()

    # 4. 출력 - 메시지 마다 말풍선 (내 메시지 🙋)
    for 메시지번호,보낸사람, 내용, 시간 in 메시지목록:
        아바타 = "🙋" if 보낸사람 == 나 else "👤"
        with st.chat_message(보낸사람, avatar=아바타):
            st.write(f"**{보낸사람}**  {시간}")
            st.write(내용)
            st.write("메시지번호:",메시지번호)
                                # key=수정21
            if st.button("수정",key=f"수정{메시지번호}"):
                pass
                                # key=삭제21
            if st.button("삭제",key=f"삭제{메시지번호}"):
                pass

    # key  속성 - 화면(스트림릿) 보여주는 구별 설정
    # DB - primary key, unique


    # 5. 입력: 새 메시지 보내기
    메시지 = st.chat_input("메시지를 입력하세요")

    if 메시지 and 메시지.strip():   # 비어있거나 앞뒤공백제거
        마우스.execute("""
            insert into
                msg (채팅방,보낸사람,내용)
            values
                (?, ?, ?)
        """, (채팅방이름, 나, 메시지))

        # 확정
        db저장소.commit()

        # 보낸 메시지를 바로 보이게 설정
        st.rerun()





#--------------------------------------------------


  # 뭐지?가 중복적으로 하나의 뭐지를
    # 삭제하려고 한다
    # 데이터베이스에서 삭제!명령어
    # delete  from  테이블명
    # sqlite3

    # delete from 테이블명
    # 전체 삭제

    # delete from 테이블명
    # where 를 하고 컬럼명 = 값
    # 테이블 안에 같은 내용이
    # 다!! 지워진다.
    # where 조건을 준다
    # 유일한 번호를 이용해서 조심히
    # 삭제한다. (primary key)

    # 마우스.execute("""
    #     delete from
    #         msg
    #     where
    #         메시지번호 = '2'

    # """)

    # 메시지를 수정
    # update  테이블명
    # set
    #   어떤칸(컬럼) = "수정할 내용"
    # where
    #   primary key 컬럼 = 번호

    # 마우스.execute("""
    #     update
    #         msg
    #     set
    #         내용 = '내일은'
    #     where
    #         메시지번호 = 23
    # """)

    # db저장소.commit()
