import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_PATH = BASE_DIR / "dev" / "employees.csv"

df = pd.read_csv(CSV_PATH)

st.dataframe(csv)

"""
문제 2 — DataFrame 조건 필터링
Python 점수가 85점 이상이고, 경력이 5년 미만인 직원의 이름, 부서, Python 점수만 출력하시오.

loc와 & 연산자를 사용해.
"""

df.loc[
    (df["python_score"]>=85) & (df["experience"] < 5),
    ["name", "department"]
]

df.loc[
    (df["departmen"] == "AI") | (df["salary"] >= 60000),
    ["name", "department", "salary"]
]