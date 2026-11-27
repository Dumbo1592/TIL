    import pandas as pd
    import streamlit as st
    # 예측을 할 수 있도록 도와주는 도구를 가져온다.
    from sklearn.linear_model import LinearRegression as sk
    from pathlib import Path

    st.set_page_config(layout="wide")

    file_path = Path(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\CAFE_DATA.csv")

    try:
        cafeData = pd.read_csv(file_path)

    except FileNotFoundError:
        st.error("파일을 찾을 수 없습니다.")

    except Exception as e:
        st.error(f"파일 읽기 실패: {e}")

    else:
        # st.dataframe(cafeData, width="stretch", height=600)
        st.write(cafeData.shape)
        st.dataframe(cafeData)
        
        # st.dataframe(cafeData[["SALES_CD", "MLSFC_CD", "PAYMENT_PRICE"]].head(3))
        st.write(cafeData.isna().sum())
        st.write(cafeData.duplicated().sum())
        
        매출 = cafeData[cafeData["SALES_CD"] == "매출"].copy()
        반품 = cafeData[cafeData["SALES_CD"] == "반품"].copy()

        # 무엇이 바꿨고, 결과가 맞는가?
        # st.write("원본 행 수:", len(cafeData))
        # st.write("매출 행 수:", len(매출))
        # st.write("반품 행 수:", len(반품))
        # st.write(f"총 매출: {매출["PAYMENT_PRICE"].sum():,.0f}")
        # st.write(f"반품액:{반품["PAYMENT_PRICE"].sum():,.0f}")
        # st.write(f"순 매출:{매출["PAYMENT_PRICE"].sum() - 반품["PAYMENT_PRICE"].sum():,.0f}")

        # st.write(매출["MLSFC_CD"].unique(), " ", )
        
        상품군 = 매출.groupby("MLSFC_CD")["PAYMENT_PRICE"].sum().sort_values(ascending=False)
        
        # 가끔 데이터 타입이 안 맞아서 print하다가 타입 에러가 발생
        # 어떤 타입이든 문자로 바꿔서 출력해라! to_string
        
        # st.write(상품군.style.format({"PAYMENT_PRICE:":"{:,.0f}"}))

        # 예측을 할 때
        # 커피 판매기록 선택
        커피 = 매출[매출["MLSFC_CD"] == "커피"].copy()

        # 학습할 자료를 준비
        # 몇 잔인가? 실제 얼마인가?
        
        # 과거에 몇 잔 팔았나요
        판매수량 = 커피[["SLE_CO"]]
        # 그때 얼마 받았나요
        결제금액 = 커피[["PAYMENT_PRICE"]]

        # 공부할 학생
        학생 = sk()

        # 학생 학습한다. 학습할 때 필요한 과거 자료들 넣어준다
        학생.fit(판매수량, 결제금액)

        새문제 = pd.DataFrame({
            "SLE_CO" : [3],
        })
        
        예측결과 = 학생.predict(새문제)

        st.write(예측결과)

        # 같은 상품군으로 묶고 결제 금액을 더 해서 출력
        # 큰 순서대로 정렬합니다.
        
        # 구조확인
        # SALES_CD - 매출/반품 구분
        # MLSFC_CD - 상품군: 커피,케이크 등
        # SLE_CO - 해당 행의 수량
        # PAYMENT_PRICE - 해당 행의 결제금액
        # PRIPT_NO - 영수증 번호
        # RESVE_DT - 예약 일시로 해석하는 열
        # DSECNT_RT - 할인율로 해석하는 열
        
        # 예측을 하려면 도구가 필요하다!
        # pip install scikit-learn
        # 학습 -> 예측 -> 검증

        # 사람이 규칙을 만들어서 사용했지만
        # 데이터가 많아지기 때문에 컴퓨터가 스스로 규칙을 찾는 것!

        # 과거의 데이터(정답 + 문제)
        # 머신러닝 : 데이터 + 정답 = 컴퓨터가 규칙을 찾음

        # 학습 fit()
        # 예측 predict()

        # 단체 주문이 들어왔는데 대략적으로 커피 3잔이면 얼마 쯤 나올까요
