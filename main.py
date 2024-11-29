import streamlit as st
from langchain_openai import ChatOpenAI

###### 모듈 #####
from DATA.UserDataController import userProfile
# from VectorStore.H100
###### ### #####
### 화면 구성 ### 상단 바 이름
st.set_page_config(page_title="Health100")
### 화면 구성 ### 타이틀 이름
st.title("Health100")
### 화면 구성 ### 사이드 바 구성
with st.sidebar:
    name = st.text_input("이름",value="홍길동")

    age = st.number_input("나이", value=20, min_value=0, max_value=200, step=1)

    height = st.number_input("키", value=170, min_value=0, max_value=400, step=1)
    
    weight = st.number_input("몸무게", value=70, min_value=0, max_value=500, step=1)

    disease = st.pills("질환", ["고혈압", "당뇨", "관절염"], selection_mode="multi")
    desease_result = "없음" if len(disease)==0 else disease

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    pass

user = userProfile(name, age, height, weight, desease_result)
### 필요 함수 구성 #######################################

# OpenAI API로 답변 생성 함수

def generate_response(input_text):
    llm = ChatOpenAI(temperature=0,
                     model_name="gpt-3.5-turbo-0125",
                     api_key= openai_api_key)
    st.info(llm.predict(input_text))

########################################################

# main 페이지 구성
# 채팅 부분
with st.form("Question"):
    # 첫페이지가 실행될 때 보여줄 질문
    text = st.text_area("질문 입력:", f"{user} \n\n 운동 추천해주세요")
    # 보내기 버튼
    submitted = st.form_submit_button("보내기")

    # API Key 확인 후 답변 생성
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)