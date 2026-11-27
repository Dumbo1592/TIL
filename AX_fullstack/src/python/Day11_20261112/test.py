import pandas as pd

원본데이터 = pd.read_csv(r"C:\Users\bdt15\OneDrive\Desktop\Work_Space\Python\Kant_Assignment\AX_fullstack\dev\bcycl.csv", encoding="cp949")

print("전체 행 수:", 원본데이터.shape)
print()
print(원본데이터.head(5))
원본데이터.info()

# 데이터가 비어있는게 있는지 확인
print(원본데이터.isna().sum())

# 빈 값 발견 -> 실제 행 확인 -> 처리 방법 결정
# 지울까? 채울까? 남길까?
# 출발 도착 기준이 함께 있음
# 이용 시간이 비어있음
# 항상 원본은 건드리지말고! 무조건 copy()
# 원본을 남기면 어떤 처리 때문에 결과가 달라지는지 확인

# 출발시간 기준만 선택하고 복사
출발 = 원본데이터[원본데이터["집계_기준"] == "출발시간"].copy()
print("원본: ", len(원본데이터))
print("분석용: ", len(출발))

# copy() 메모리 안에 작업용 데이터가 만들어진다.
# CSV 파일이 하나 더 생기는 건 아니다

# 분석 - 언제 많이 탈까?
# 이용이 집중된 시간은 언제인가요?
# 묶어서 계산을 한다
# 시간대로 그룹 지어서 확인한다.

# 원래 합계
# 출발 그 안에서 전체_건수 출력
원래 = 출발["전체_건수"].sum()

# 전체 이용: 114769
print()
print("전체 이용:", 원래)

print(출발["기준_시간대"].unique())

# 시라는 새로운 컬럼을 만들어서
# 시간별을 저장 해보도록 함
출발["시"] = 출발["기준_시간대"]

#print(출발["시"].unique())

# 같은 시 끼리 묶어서 이용 건수 더하기
시간별 = 출발.groupby("시")["전체_건수"].sum()

print(시간별)

# 정렬
# - 기본값 오름차순

print()
print(시간별.sort_values(ascending=False).head(5))

# 어디서 많이 탈까?
# 상황
# - 출발이 많은 대여소
# 출발 건수가 많은 대여소 확인
# 인사이트
# - 
# 액션

출발["시"] = 출발["기준_시간대"].sum()


"""
copy()	원본과 복사본
dropna() / fillna()	빈 값 삭제 / 빈 값 채우기
duplicated() / drop_duplicates()	중복 확인 / 중복 제거
drop_duplicates() / drop_duplicates(keep="last") / drop_duplicates(keep=False)	첫 번째 유지 / 마지막 유지 / 중복된 행 전부 삭제
drop_duplicates() / drop_duplicates(subset=["메뉴"])	모든 열 기준 / 특정 열 기준
str.strip()	문자열 앞뒤 공백 제거
value_counts() / count() / len()	값별 개수 / 빈 값 제외 개수 / 빈 값 포함 개수
duplicated().sum()	중복으로 표시된 행 개수
print() / st.write() / st.dataframe()	터미널 출력 / 웹 화면 출력 / 웹 표 출력

df.head(5)	앞에서 5행 확인
df.tail(5)	뒤에서 5행 확인
df.sample(2)	무작위로 2행 확인
df.info()	열 이름, 자료형, 결측치가 아닌 값의 개수 확인
df.describe()	숫자 열의 개수·평균·표준편차·최솟값·최댓값 등 확인

df.shape	(행 개수, 열 개수)
df.columns	열 이름
df.index	행의 인덱스
df.dtypes	열별 자료형
df.size	전체 원소 개수
df.empty	데이터가 비어 있는지 확인

df["나이"].sum()	합계
df["나이"].mean()	평균
df["나이"].median()	중앙값
df["나이"].min()	최솟값
df["나이"].max()	최댓값
df["나이"].std()	표준편차
df["나이"].var()	분산

df.count()	열별 결측치를 제외한 값의 개수
df.isna()	결측치이면 True
df.notna()	결측치가 아니면 True
df.isna().sum()	열별 결측치 개수
df.dropna()	결측치가 있는 행 삭제
df.fillna(0)	결측치를 0으로 채움

df.sort_values("나이")	나이를 기준으로 오름차순 정렬
df.sort_values("나이", ascending=False)	나이를 기준으로 내림차순 정렬
df.sort_index()	행 인덱스를 기준으로 정렬
df.drop(columns=["점수"])	점수 열 삭제
df.rename(columns={"이름": "성명"})	열 이름 변경
df.drop_duplicates()	중복 행 제거
df.reset_index(drop=True)	기존 인덱스를 버리고 0부터 다시 설정
df.astype({"나이": "float"})	나이 열의 자료형 변경

df["이름"]	이름 열 선택
df[["이름", "나이"]]	여러 열 선택
df.loc[0, "이름"]	인덱스와 열 이름으로 값 선택
df.iloc[0, 1]	행·열 위치로 값 선택, 위치는 0부터 시작
df.query("나이 >= 23")	조건에 맞는 행 선택
df["나이"].unique()	중복을 제외한 값 목록
df["나이"].nunique()	서로 다른 값의 개수
df["나이"].value_counts()	값별 등장 횟수
df.groupby("나이")["점수"].mean()	나이별 평균 점수
df["나이"].apply(lambda x: x + 1)	각 값에 함수를 적용
"""