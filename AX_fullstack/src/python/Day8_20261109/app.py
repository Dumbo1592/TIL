import streamlit as st

#Streamlit
# - 파이썬으로 웹사이트나 웹 애플리케이션을 쉽게 만들 수 있게 도와주는 도구
# 1. 현재 파일이 실행될 때

# st.title("AI 리터러시 수업")
# st.header("AI란?")
# st.image(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\1_ai.png")
# st.write("ai 리터러시\n 1. 기초 지식\n2. 비판적 평가 기술\n3. 기술적 숙련도\n4. 맥락적 및 윤리적 이해 ")

# 2. 위의 내용을 실행
# 내 컴퓨터 안에서만 볼 수있는
# 터미널 켜고 -> cmd -> python -m streamlit run app.py

#3. 항상 코드를 작성하고 나면 꼭 저장하기
# ctrl + s
# st.header("규칙 기반 AI란?")
# st.write("Rule-Based AI")
# st.image(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\1-1_rule.png")
# st.write("사람이 정한 규칙을 따르는 인공지능")

# # 머신러닝
# st.header("머신러닝(Machine Learning)")
# st.image(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\2_ml.png")
# st.write("데이터에서 규칙이나 패턴을 학습하는 기술")
# st.write("사람이 모든 규칙을 직접 작성하지 않고 컴퓨터 데이터를 보고 패턴을 찾는다")

# st.header("딥러닝(Deep Learning)")
# st.image(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\3_dl.png")
# st.write("복잡한 데이터에서도 특징과 패턴을 학습할 수있는 기술")
# st.write("얼굴인식,음성인식, 제품불량 이미지 판별,의료 영상 분석지원")
# st.write("여러 층의 인공신경망을 이용하는 머신러닝 기술")

# st.header("생성형 AI란?")
# st.image(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\4_genai.png")
# st.write("생성형 AI는 학습한 패턴을 바탕으로 글, 이미지, 음악, 영상 같은 새로운 콘텐츠를 만들어 내는 인공지능이다")
# #웹사이트에 그림이나 이미지를 올릴 때 사용하는 명령어
#image("파일명 경로.확장자")
# 파이썬 streamlit에 대해서 검색해보기
# 생성형 AI란?
# LLM이란?
# 토큰이란?
# 프롬프트란

sections = [
    {"title": "AI란?", "text":"1. 기초 지식\n2. 비판적 평가 기술\n3. 기술적 숙련도\n4. 맥락적 및 윤리적 이해"},
    {"title": "머신러닝", "text": "데이터에서 패턴을 학습하는 기술"},
    {"title": "딥러닝", "text": "여러 층의 신경망으로 학습하는 기술"},
    {"title": "생성형 AI", "text": "새로운 콘텐츠를 생성하는 기술"},
]

ai_image = [
    r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\1_ai.png",
    r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\2_ml.png",
    r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\2_ml.png",
    r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\3_dl.png",
    r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\AI_단어_이미지\4_genai.png"
]

st.title("AI 리터러시 수업")

for i, section in enumerate(sections):
    st.header(section["title"])
    st.write(section["text"])
    st.image(ai_image[i])