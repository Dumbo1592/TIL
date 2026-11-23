import pandas as pd

# pandas = 표를 짧은 코드로 읽고, 고치고, 계산하게 해주는 파이썬 도구

# data = [80, 90, 80, 90, 50, 60]

# total = 0
# for score in data:
#     total += score
# avg = total / len(data)
# print(avg) #75.0

#sum 사용
# total = sum(data)
# print(total/len(data)) #75.0

# print(sum[80,90,None,70])
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
# print(sum(["12000","8000","8000","5000"]))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 현실의 데이터에는 빈 값과 글자 숫자가 섞여 있다, 표로 만들어서 눈으로 보고 정리하기 위해서 pandas 사용

#DataFrame = 행과 열로 이루어진 표 전체(엑셀 시트)
#Series = 표에서 한 줄만 뽑은 것
def Overview(df):
    print("행*열:", df.shape)
    print(df.head(2))
    
student = {
    "이름" : ["철수", "영희", "민수"],
    "점수" : [80, 90, 70],
    "출석" : ["출석", "출석", "결석"]
}

# 딕셔너리 = 키로 값을 찾는다. 학생["점수"]
# 리스트 = 줄을 세워 번호로 찾는다. 학생["이름"][1] -> 영희

# df = pd.DataFrame(student)
# print(df.shape)
# print(df.head(2))
# print(df["점수"])

# Overview(df)
# notna() 값이 있으면 True

# print(df.isna().sum())
# print(df["점수"].isna())
# print(df["점수"].notna())
# print(df[df["점수"].isna()])
# print(df[df["점수"].notna()])

# 과일 = {"과일": ["사과", "바나나", "딸기", "포도"],
#         "가격": [3000, 2000, 8000, 6000],
#         "재고": [10, 25, 5, 12]}

# df = pd.DataFrame(과일)
# print(df.shape)
# print(df.loc[:1])

# 동아리 = {"이름": ["가","나","다","라","마"],
#           "학년": [1, 2, 1, 3, 2],
#           "출석": ["출석","결석","출석","출석","결석"]}

# df = pd.DataFrame(동아리)
# print(df["학년"])
# print(df[["이름", "학년"]].head(2))

# 점수표 = {"이름": ["가","나","다","라"],
#           "점수": [90, None, 75, None]}

# df = pd.DataFrame(점수표)

# print(df["이름"].isna().sum())
# print(df["점수"].isna().sum())
# print(df["점수"].notna())
# print(df[df["점수"].notna()])

# 대출 = {"책": ["a","b","c","d","e"],
#         "일수": [7, 14, 7, 3, 14]}

# df = pd.DataFrame(대출)
# print(df.iloc[1:4])
# print(df.loc[1:4])

# 편의점 = {"상품": ["물","라면","과자","우유","빵","커피","껌","콜라","김밥","음료"],
#           "수량": [2,1,3,99,1,2,1,2,1,1],
#           "가격": [1000,1500,1800,2500,2000,2200,1000,2000,3000,1800]}

# df = pd.DataFrame(편의점)

# print(df.tail(3))
# print(df[df["수량"] > 5])
# print(df.isna().sum())

설문 = {"이름": ["가","나","다","라","마"],
        "나이": [20, None, 31, 25, None],
        "점수": [85, 90, 120, 70, 95]}

df = pd.DataFrame(설문)

# print(df[df["나이"].isna()])
print(df[df["점수"] > 100])
