from pathlib import Path
import pandas as pd
import platform
import matplotlib.pyplot as plt
import seaborn as sns

data_path = Path(__file__).resolve().parents[3] / 'dev' / 'titanic.csv'
titanic = pd.read_csv(data_path)

print("전체 행 수:", len(titanic))

# 원본을 보존하고, 그래프에서 사용할 데이터의 결측치를 처리합니다.
df = titanic.copy()
df['age'] = df['age'].fillna(df['age'].mean())
df['fare'] = df['fare'].fillna(df['fare'].median())
df = df.dropna(subset=['age', 'fare', 'class', 'survived'])
df['fare'] = df['fare'].clip(lower=0)

os_name = platform.system()
if os_name == "Windows":
    plt.rcParams['font.family'] = 'Malgun Gothic' # 윈도우
elif os_name == "Darwin":
    plt.rcParams['font.family'] = 'AppleGothic'   # 맥북
else:
    plt.rcParams['font.family'] = 'NanumGothic'   # 기타(코랩 등)

plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 도화지(Figure)와 3개의 액자(Axes) 준비
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('타이타닉 탑승객 데이터 분석 (데이터 정제 및 시각화)', fontsize=16)

# [히스토그램] 탑승객 나이 분포
axes[0].hist(df['age'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title('탑승객 나이 분포 (결측치 평균 대체 후)')
axes[0].set_xlabel('나이 (세)')
axes[0].set_ylabel('승객 수 (명)')

# [박스 플롯] 티켓 등급에 따른 요금 이상치 확인
# 박스(상자) 바깥쪽에 외롭게 찍혀 있는 점들이 바로 일반적인 범위를 벗어난 '이상치'들입니다.
sns.boxplot(x='class', y='fare', hue='class', data=df, ax=axes[1], palette='Set2', legend=False)
axes[1].set_title('티켓 등급별 요금 분포 (박스 플롯)')
axes[1].set_xlabel('티켓 등급')
axes[1].set_ylabel('티켓 요금 (달러)')

# [산점도] 나이와 클리닝된 요금의 관계
scatter = axes[2].scatter(
    df['age'], 
    df['fare'], 
    c=df['survived'], # 생존 여부(1: 생존, 0: 사망)에 따라 색상이 다름
    cmap='coolwarm',
    s=df['fare'] / 2, # 요금이 비쌀수록 원이 조금 더 큼
    alpha=0.7
)
axes[2].set_title('나이 vs 티켓 요금 (빨간색: 생존, 파란색: 사망)')
axes[2].set_xlabel('나이 (세)')
axes[2].set_ylabel('티켓 요금 (달러)')

fig.colorbar(scatter, ax=axes[2], label='생존 여부')

plt.tight_layout()
plt.show()
