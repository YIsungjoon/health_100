import streamlit as st
import pandas as pd
import os

from DATA.UserData import save_user_data, authenticate_user
from LLMs.openai import generate_response
###### 파일 경로 설정 #####
USER_DB_FILE = "./data/user_data.csv"

###### 화면 구성 #####
st.set_page_config(page_title="Health100")
st.title("Health100")
st.image("./img/backgroundimg.webp")

### 세션 상태 초기화 ###
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

### 사이드바 구성 ###
with st.sidebar:
    st.header("회원 관리")
    mode = st.radio("회원 모드 선택", ["로그인", "회원가입"])

    # OpenAI API Key 입력
    openai_api_key = st.text_input("OpenAI API Key", type="password")

### 메인 페이지 ###
if mode == "회원가입":
    st.subheader("회원가입")
    
    # 회원 정보 입력
    name = st.text_input("이름", value="홍길동")
    age = st.number_input("나이", value=20, min_value=0, max_value=200, step=1)
    height = st.number_input("키", value=170, min_value=0, max_value=400, step=1)
    weight = st.number_input("몸무게", value=70, min_value=0, max_value=500, step=1)
    disease = st.multiselect("질환", ["고혈압", "당뇨", "관절염"])
    desease_result = ", ".join(disease) if disease else "없음"
    
    # 회원가입 버튼
    if st.button("회원가입"):
        new_user = {"NAME": name, "측정연령수": age, "신장(cm)": height, "체중(kg)": weight, "질환": desease_result}
        user_id = save_user_data(new_user)
        st.success(f"회원가입 완료! 부여된 ID는 '{user_id}' 입니다.")

elif mode == "로그인":
    st.subheader("로그인")

    # 로그인 상태 확인
    if not st.session_state.logged_in:
        # 로그인 정보 입력
        user_id = st.text_input("ID")
        name = st.text_input("이름")
        
        # 로그인 버튼
        if st.button("로그인"):
            user = authenticate_user(user_id, name)
            if user is not None:
                st.session_state.logged_in = True
                st.session_state.current_user = user
                st.success(f"로그인 성공! 환영합니다, {name}님. 로그인 버튼을 한 번 더 눌러주세요")
            else:
                st.error("로그인 실패! ID 또는 이름을 확인해주세요.")
    else:
        # 로그인 후 화면
        user = st.session_state.current_user
        st.success(f"로그인 중: {user['NAME'].values[0]}님 (ID: {user['ID'].values[0]})")
        
        # 사용자 정보 표시
        st.write("회원 정보:")
        st.write(user[["ID","NAME","측정연령수","신장(cm)","체중(kg)"]])
        
        
        
        # 운동 추천 질문
        with st.form("Question"):
            text = st.text_area("질문 입력:", f"{user['NAME'].values[0]} \n\n 운동 추천해주세요")
            submitted = st.form_submit_button("보내기")
            
            # API Key 확인 후 응답 생성
            if not openai_api_key.startswith("sk-"):
                st.warning("Please enter your OpenAI API key!", icon="⚠")
            if submitted and openai_api_key.startswith("sk-"):
                response = generate_response(text, openai_api_key)
                st.info(response)

        # 로그아웃 버튼
        if st.button("로그아웃"):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.warning("로그아웃 되었습니다.")
