import streamlit as st
import random
from sklearn.linear_model import LogisticRegression

# ---- 더하기 함수 ----
def add(a, b):
    return a + b                                            # 두 수를 더해서 돌려줘요

# ---- 과거 기록 (새로고침해도 유지되게 session_state에 저장) ----
if "체력" not in st.session_state:
    st.session_state.체력 = [[10], [20], [30], [70], [80], [90]]                # 힌트: 내 체력(HP)
    st.session_state.행동 = ["도망", "도망", "도망", "싸운다", "싸운다", "싸운다"]  # 정답
체력 = st.session_state.체력
행동 = st.session_state.행동

# ---- 화면 ----
st.title("🧟 좀비 게임, 싸울까 도망갈까?")

# ---- 랜덤 체력 뽑기 ----
if "입력체력" not in st.session_state:
    st.session_state.입력체력 = 50
if st.button("🎲 랜덤 체력 뽑기"):
    st.session_state.입력체력 = random.randint(0, 100)     # 입력칸보다 먼저 값을 바꿔야 반영돼요
입력체력 = st.number_input("내 체력(HP)", min_value=0, max_value=100, key="입력체력")

# ---- 공부시키기 ----
모델 = LogisticRegression()
모델.fit(체력, 행동)     # '점수 = 기울기×체력 + 절편'의 기울기와 절편을 찾아요
싸움칸 = list(모델.classes_).index("싸운다")    # classes_는 정답 글자를 정렬한 순서 → "싸운다" 칸 번호


if st.button("예측하기"):
    결과 = 모델.predict([[입력체력]])                       # 답 (확률 0.5 초과 쪽 글자)
    확률 = 모델.predict_proba([[입력체력]])                 # [[도망, 싸운다]] 모양의 확률
    싸움확률 = float(확률[0][싸움칸])                       # 0~1, 첫 줄의 싸운다 칸

    # 결과 출력
    if 결과[0] == "싸운다":
        st.write("⚔️ 좀비와 싸울 것 같아요!")
    else:
        st.write("🏃 도망갈 것 같아요!")

    st.write("싸울 확률:", round(싸움확률 * 100), "%")
    st.progress(싸움확률)                                   # 확률을 막대로 보여줘요

    # 확률 3단계 (0.5 하나 대신 내 기준으로 나누기)
    # 30% 미만 이면 도망간다  error()
    # 30% 이상 이면 포션먹자! warning()
    # 70% 이상 이면 돌격! 싸우자! success()
    if 싸움확률 >= 0.7:
        st.success("돌격! 싸우자!")
    elif 싸움확률 >= 0.3:
        st.warning("포션먹자!")
    else:
        st.error("도망간다!")

# ---- 체력별 싸울 확률 그래프 ----
st.subheader("📈 체력별 싸울 확률")
전체체력 = [[hp] for hp in range(101)]
전체확률 = 모델.predict_proba(전체체력)[:, 싸움칸] * 100    # 0~100 체력마다 싸울 확률(%)
st.line_chart({"싸울 확률(%)": list(전체확률)})            # 가로축 번호 = 체력

# ---- 내 선택 기록 추가 → 다시 공부 ----
st.subheader("📝 내 실제 선택 기록하기")
내선택 = st.radio("이 체력에서 나는 실제로…", ["싸운다", "도망"], horizontal=True)
if st.button("기록 추가"):
    st.session_state.체력.append([입력체력])
    st.session_state.행동.append(내선택)
    st.rerun()                                              # 새 기록으로 바로 다시 공부해요

st.write("지금까지 기록:", len(행동), "개")
st.dataframe({"체력": [hp[0] for hp in 체력], "행동": 행동})
