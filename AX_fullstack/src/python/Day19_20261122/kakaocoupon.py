import sqlite3 as db
import streamlit as st

con = db.connect("회원")
마우스 = con.cursor()

마우스.execute("""
    CREATE TABLE IF NOT EXISTS members(
        회원번호 INTEGER PRIMARY KEY AUTOINCREMENT,
        아이디 TEXT NOT NULL UNIQUE,
        비밀번호 TEXT NOT NULL,
        이름 TEXT NOT NULL,
        전화번호 TEXT NOT NULL UNIQUE
    )
""")

마우스.execute("""
    CREATE TABLE IF NOT EXISTS products(
        상품번호 INTEGER PRIMARY KEY AUTOINCREMENT,
        상품코드 TEXT NOT NULL UNIQUE,
        상품이름 TEXT NOT NULL,
        가격 INTEGER NOT NULL,
        상품설명 TEXT
    )
""")

마우스.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        주문번호 INTEGER PRIMARY KEY AUTOINCREMENT,
        구매자아이디 TEXT NOT NULL,
        상품코드 TEXT NOT NULL,
        수량 INTEGER NOT NULL,
        결제금액 INTEGER NOT NULL,
        배송주소 TEXT NOT NULL,
        배송메모 TEXT
    )
""")

st.title("톡톡 쇼핑")
가입탭, 로그인탭, 등록탭, 쇼핑탭, 주문탭 = st.tabs(["회원가입", "로그인", "상품등록", "쇼핑하기", "주문내역"])

with 가입탭:
    with st.container(border=True):
        새아이디 = st.text_input("아이디", key="새아이디").strip()
        새비밀번호 = st.text_input("비밀번호", type="password", key="새비밀번호").strip()
        새이름 = st.text_input("이름", key="새이름").strip()
        새전화번호 = st.text_input("전화번호", key="새전화번호").strip()

    if st.button("가입하기"):
        if not 새아이디 or not 새비밀번호 or not 새이름 or not 새전화번호:
            st.warning("아이디, 비밀번호, 이름, 전화번호는 꼭 입력하세요")
        else:
            마우스.execute(
                "SELECT 아이디 FROM members WHERE 아이디 = ?",
                (새아이디,)
            )

            같은아이디 = 마우스.fetchone()

            마우스.execute(
                "SELECT 전화번호 FROM members WHERE 전화번호 = ?",
                (새전화번호,)
            )

            같은전화번호 = 마우스.fetchone()

            if 같은아이디:
                st.warning("이미 사용 중인 아이디에요")
            elif 같은전화번호:
                st.warning("이미 가입된 전화번호에요")
            else:
                마우스.execute(
                    "INSERT INTO members (아이디, 비밀번호, 이름, 전화번호) VALUES (?,?,?,?)",
                    (새아이디,새비밀번호,새이름,새전화번호)
                )
                con.commit()
                st.success(f"{새이름}님 가입완료!")

with 로그인탭:
    with st.container(border=True):
        아이디 = st.text_input("아이디", key="로그인_아이디").strip()
        비밀번호 = st.text_input("비밀번호", type="password", key="로그인_비밀번호").strip()

        마우스.execute(
            "SELECT 아이디, 비밀번호, 이름 FROM members WHERE 아이디 = ?",
            (아이디,)
        )

        회원 = 마우스.fetchone()

        로그인아이디 = ""
        if not 아이디:
            st.write("아이디와 비밀번호를 입력하세요")
        elif not 회원:
            st.warning("없는 회원입니다")
        elif 회원[1] != 비밀번호:
            st.warning("비밀번호가 틀렸어요")
        else:
            로그인아이디 = 회원[0]
            st.success(f"{회원[2]}님 로그인 중")

with 등록탭:
    with st.container(border=True):
        상품코드 = st.text_input("상품코드", key="등록_코드").strip()
        상품이름 = st.text_input("상품이름", key="등록_이름").strip()
        가격 = st.text_input("가격", key="등록_가격").strip()
        상품설명 = st.text_input("상품설명", key="등록_설명").strip()

        if st.button("상품등록"):
            if not 상품코드 or not 상품이름 or not 가격:
                st.warning("상품코드, 상품이름, 가격은 꼭 입력하세요")
            elif not 가격.isdecimal() or int(가격) <= 0:
                st.warning("가격은 0보다 큰 정수로 입력하세요")
            else:
                마우스.execute(
                    "SELECT 상품코드 FROM products WHERE 상품코드 = ?",
                    (상품코드,)
                )

                같은상품 = 마우스.fetchone()

                if 같은상품:
                    st.warning("이미 있는 상품코드에요")
                else:
                    마우스.execute(
                        "INSERT INTO products (상품코드, 상품이름, 가격, 상품설명) VALUES (?,?,?,?)",
                        (상품코드, 상품이름, int(가격), 상품설명)
                    )
                    con.commit()
                    st.success(f"{상품이름} 등록완료")

with 쇼핑탭:
    with st.container(border=True):
        if not 로그인아이디:
            st.warning("로그인 탭에서 먼저 로그인하세요")
        else:
            마우스.execute(
                "SELECT 상품코드, 상품이름, 가격 FROM products",
            )
            
            상품목록 = 마우스.fetchall()

            상품코드목록 = []

            for 상품 in 상품목록:
                st.write(f"[{상품[0]}] {상품[1]} - {상품[2]}원")
                상품코드목록.append(상품[0])

            if not 상품목록:
                st.warning("등록된 상품이 없어요!")
            else:
                고른코드 = st.selectbox("상품코드", 상품코드목록)
                수량 = st.selectbox("수량", [1,2,3,4,5])

                마우스.execute(
                    "SELECT 상품이름, 가격 FROM products WHERE 상품코드 = ?",
                    (고른코드,)
                )

                고른상품 = 마우스.fetchone()
                결제금액 = 고른상품[1] * 수량
                st.write(f"{고른상품[0]} {수량}개 = {결제금액}원")

                배송주소 = st.text_input("배송주소", key="주문_취소").strip()
                배송메모 = st.text_input("배송메모", key="주문_메모").strip()

                if st.button("구매하기"):
                    if not 배송주소:
                        st.warning("배송주소를 입력하세요")
                    else:
                        마우스.execute(
                            "INSERT INTO orders (구매자아이디, 상품코드, 수량, 결제금액, 배송주소, 배송메모) VALUES (?,?,?,?,?,?)",
                            (로그인아이디,고른코드,수량,결제금액,배송주소,배송메모)
                        )
                        con.commit()
                        st.success(f"{고른상품[0]}, {수량} 구매완료")
            
