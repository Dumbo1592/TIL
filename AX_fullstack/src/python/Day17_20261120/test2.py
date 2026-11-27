import streamlit as st
import random
from sklearn.linear_model import LogisticRegression

study_time = [[1],[2],[3],[4],[5],[6],[7]]
study_data = ["불합격","불합격","불합격","불합격","불합격","불합격","합격"]

st.title("공부시간을 통해 합격, 불합격을 예측해드립니다")

n = st.number_input("공부시간",min_value=0,max_value=24,value=random.randint(0,24))

model = LogisticRegression()
model.fit(study_time, study_data)

if st.button("랜덤시간"):
    output = model.predict([[n]])
    pro = model.predict_proba([[n]])
    합격칸 = list(model.classes_).index("합격")
    합격확률 = float(pro[0][합격칸])
    
    if output[0] == "합격":
        st.write("합격했습니다")
    else:
        st.write("불합격했습니다")
        
    st.write("합격 확률:", round(합격확률 * 100), "%")

    if 합격확률 >= 0.7:
        st.success("합격")
    elif 합격확률 >= 0.3:
        st.warning("애매")
    else:
        st.error("불합격")
        
print("done")