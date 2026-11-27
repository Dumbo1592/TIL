# from/import: 다른 모듈의 기능 가져오기. Path는 파일 경로를 다루는 클래스예요.
from pathlib import Path

import streamlit as st  # as: streamlit을 st라는 짧은 이름으로 사용

# set_page_config: 브라우저 탭 제목, 아이콘, 화면 너비 설정
st.set_page_config(
    page_title="AI Dictionary",
    page_icon="✦",
    layout="wide",
)

# __file__: 현재 코드 파일 경로 / resolve(): 절대 경로로 변환
# parents[3]: 네 단계 위 폴더(AX_fullstack) / 경로의 / 연산자: 하위 경로 연결

IMAGE_DIR = Path(__file__).resolve().parents[3] / "dev" / "AI_단어_이미지"

# 리스트([]) 안에 용어별 딕셔너리({키: 값})를 저장해요.
TOPICS = [
    {
        "title": "인공지능",
        "english": "Artificial Intelligence",
        "category": "기초 개념",
        "image": "1_ai.png",
        "description": "학습, 추론, 문제 해결 등 지능이 필요한 작업을 수행하는 기술이에요.",
        "example": "음성 비서, 추천 시스템, 이미지 인식",
    },
    {
        "title": "규칙 기반 AI",
        "english": "Rule-Based AI",
        "category": "기초 개념",
        "image": "1-1_rule.png",
        "description": "사람이 미리 정한 조건과 규칙에 따라 판단하는 방식이에요.",
        "example": "온도가 30도 이상이면 냉방 켜기",
    },
    {
        "title": "머신러닝",
        "english": "Machine Learning",
        "category": "학습 기술",
        "image": "2_ml.png",
        "description": "모든 규칙을 직접 작성하는 대신, 데이터에서 패턴을 학습하는 기술이에요.",
        "example": "이메일 내용으로 스팸 여부 분류하기",
    },
    {
        "title": "딥러닝",
        "english": "Deep Learning",
        "category": "학습 기술",
        "image": "3_dl.png",
        "description": "여러 층의 인공신경망을 사용하는 머신러닝 기술이에요.",
        "example": "음성 인식, 이미지 분류",
    },
    {
        "title": "생성형 AI",
        "english": "Generative AI",
        "category": "생성형 AI",
        "image": "4_genai.png",
        "description": "학습한 패턴을 바탕으로 글, 이미지, 소리 등의 콘텐츠를 생성해요.",
        "example": "여행 일정 작성, 이미지 생성",
    },
    {
        "title": "대규모 언어 모델",
        "english": "Large Language Model · LLM",
        "category": "생성형 AI",
        "image": "5_llm.png",
        "description": "대규모 데이터로 학습해 언어를 처리하고 생성하는 모델이에요.",
        "example": "질문 답변, 문서 요약, 번역",
    },
    {
        "title": "프롬프트",
        "english": "Prompt",
        "category": "사용과 주의점",
        "image": "6_prompt.png",
        "description": "AI에 전달하는 질문, 지시, 예시 등의 입력이에요.",
        "example": "이 글을 초등학생도 이해하도록 세 문장으로 요약해 줘.",
    },
    {
        "title": "토큰",
        "english": "Token",
        "category": "사용과 주의점",
        "image": "7_token.png",
        "description": "모델이 텍스트를 처리할 때 사용하는 단위로, 단어나 단어의 일부일 수 있어요.",
        "example": "토큰 수는 입력·출력 한도와 API 비용 계산에 쓰여요.",
    },
    {
        "title": "컨텍스트",
        "english": "Context",
        "category": "사용과 주의점",
        "image": "8_context.png",
        "description": "답변을 만들 때 참고하는 대화, 지시, 문서 등의 정보예요.",
        "example": "앞서 전달한 회의록을 참고해서 질문에 답하기",
    },
    {
        "title": "할루시네이션",
        "english": "Hallucination",
        "category": "사용과 주의점",
        "image": "9_hallucination.png",
        "description": "AI가 사실과 다르거나 근거 없는 내용을 그럴듯하게 생성하는 현상이에요.",
        "example": "존재하지 않는 논문이나 출처를 제시하기",
    },
    {
        "title": "지식 컷오프",
        "english": "Knowledge Cutoff",
        "category": "사용과 주의점",
        "image": "10_cutoff.png",
        "description": "모델의 기본 학습 지식이 어느 시점까지의 정보를 반영하는지 나타내요.",
        "example": "이후의 소식은 검색 등으로 별도 확인해야 할 수 있어요.",
    },
]

# markdown: 마크다운으로 글 표시. 여기서는 HTML의 style 태그로 CSS를 적용해요.
# CSS: padding은 안쪽 여백, margin은 바깥 여백, border-radius는 모서리 둥글기

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1250px;
            padding-top: 2.5rem;
        }

        .hero {
            padding: 36px;
            margin-bottom: 28px;
            border-radius: 24px;
            background: linear-gradient(120deg, #172554, #4338ca);
            color: white;
        }

        .hero .eyebrow {
            color: #c7d2fe;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 3px;
        }

        .hero h1 {
            color: white;
            font-size: clamp(28px, 5vw, 46px);
            margin: 12px 0;
            padding: 0;
        }

        .hero p {
            color: #e0e7ff;
            margin-bottom: 0;
            line-height: 1.8;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 18px;
        }

        [data-testid="stImage"] img {
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True,  # HTML 태그를 화면에 적용하도록 허용
)

# with: 아래 들여쓴 요소들을 지정한 영역 안에 배치. sidebar는 옆쪽 메뉴예요.
with st.sidebar:
    st.title("✦ AI Dictionary")  # title: 큰 제목 표시
    st.caption("하나씩 알아가는 AI의 언어")  # caption: 작고 연한 보조 설명 표시
    st.divider()  # divider: 가로 구분선 표시
    category = st.radio(  # radio: 여러 항목 중 하나 선택, 선택한 값을 반환
        "학습 주제",
        ["전체", "기초 개념", "학습 기술", "생성형 AI", "사용과 주의점"],
    )
    st.divider()
    st.info("학습 팁\n\n용어를 읽은 뒤, 나만의 예시를 하나씩 떠올려 보세요.")  # info: 안내 상자

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">A GUIDE TO AI LITERACY</div>
        <h1>AI, 아는 만큼 쉬워집니다.</h1>
        <p>인공지능의 기초부터 생성형 AI 사용법까지.<br>
        11개의 핵심 개념을 그림과 함께 살펴보세요.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# text_input: 문자열 입력창 / placeholder: 입력 전 표시되는 안내 문구
# strip(): 앞뒤 공백 제거 / casefold(): 대소문자 구분 없이 비교하도록 변환
search = st.text_input(
    "용어 검색", placeholder="예: 머신러닝, LLM, 토큰"
).strip().casefold()

# 리스트 컴프리헨션: for와 if로 조건에 맞는 항목만 모아 새 리스트 만들기
# and: 두 조건 모두 참 / or: 하나라도 참 / not: 참·거짓 반전 / in: 포함 여부
# join(): 문자열들을 연결해서 제목·설명 등을 한꺼번에 검색
filtered_topics = [
    topic
    for topic in TOPICS
    if (category == "전체" or topic["category"] == category)
    and (
        not search
        or search in " ".join(
            [topic["title"], topic["english"], topic["description"], topic["example"]]
        ).casefold()
    )
]

# f"...{변수}...": 문자열 안에 값 삽입 / len(): 항목 개수 구하기
st.caption(f"{category} · {len(filtered_topics)}개의 개념")
st.write("")  # write: 문자열이나 데이터 등을 화면에 표시


# def: 재사용할 함수 정의. topic은 함수를 호출할 때 전달받는 용어 데이터예요.
def show_card(topic):
    with st.container(border=True):  # container: 요소를 한 영역으로 묶기, border: 테두리
        st.caption(topic["category"])
        st.subheader(topic["title"])  # subheader: 소제목 / ["title"]: 딕셔너리 값 조회
        st.caption(topic["english"])
        image_path = IMAGE_DIR / topic["image"]
        if image_path.is_file():  # if: 조건이 참이면 실행 / is_file(): 파일 존재 여부
            st.image(str(image_path), width="stretch")  # image: 이미지 표시 / str: 문자열 변환
        else:  # else: 위 조건이 거짓이면 실행
            st.warning(f"이미지를 찾을 수 없어요: {topic['image']}")  # warning: 경고 상자
        st.write(topic["description"])
        with st.expander("예시 살펴보기"):  # expander: 클릭해서 펼치거나 접는 영역
            st.write(topic["example"])


if not filtered_topics:  # 빈 리스트이면 실행
    st.info("검색 결과가 없어요. 다른 단어를 입력해 보세요.")

# for: 반복 실행 / range(시작, 끝, 간격): 0부터 끝 직전까지 2씩 증가
for start in range(0, len(filtered_topics), 2):
    columns = st.columns(2, gap="large")  # columns: 화면을 2열로 나누기 / gap: 열 사이 간격
    # [start:start + 2]: 최대 2개 항목 추출 / zip: 열과 용어를 하나씩 짝짓기
    for column, topic in zip(columns, filtered_topics[start:start + 2]):
        with column:
            show_card(topic)

st.divider()
st.caption("AI LITERACY / 이해하고, 질문하고, 확인하기")
