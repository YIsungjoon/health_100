import pandas as pd
import datetime

###### 파일 경로 설정 #####
USER_DB_FILE = "./DATA/userdata.csv"

# 오늘 날짜
today = datetime.date.today().strftime("%y%m%d")


###### 유틸 함수 #####
# 유저 데이터 불러오기
def load_user_data():
    """Load user data from the CSV file."""
    return pd.read_csv(USER_DB_FILE)

def save_user_data(new_user):
    """Save a new user to the CSV file."""
    df = load_user_data()
    # 유저 숫자 세기
    user_count = len(df)

    new_id = f"{today}-{user_count+1}"  # 유저 ID는 회원 수 기준으로 생성
    new_user["ID"] = new_id
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_csv(USER_DB_FILE, index=False)
    return new_id

def authenticate_user(user_id, name):
    """Authenticate a user with ID and name."""
    df = load_user_data()
    user = df[(df["ID"] == user_id) & (df["NAME"] == name)]
    return user if not user.empty else None

def input_check(check):
    # 입력 신호 받는 함수
    check = check
    pass


# userdata 컬럼 목록
# ['ID', 'DATE', 'NAME', '측정회차', '센터명', '연령구분', '측정장소구분명', '측정연령수',
#  '입력구분명', '등급', '측정일', '성별구분코드', '신장(cm)', '체중(kg)', '체지방율(%)',
#  '허리둘레(cm)', '이완기혈압_최저(mmHg)', '수축기혈압_최고(mmHg)', '악력_좌(kg)', '악력_우(kg)',
#  '윗몸말아올리기(회)', '반복점프(회)', '앉아윗몸말아올리기(회)', '일리노이(초)', '체공시간(초)',
#  '협응력시간(초)', '협응력실수횟수(회)', '협응력계산결과값(초)', 'BMI(kg/㎡)', '교차윗몸일으키기(회)',
#  '왕복오래달리기(회)', '10M 4회 왕복달리기(초)', '제자리 멀리뛰기(cm)', '의자에앉았다일어서기(회)',
#  '6분걷기(m)', '2분제자리걷기(회)', '의자에앉아 3M표적 돌아오기(회)', '8자보행(회)', '상대악력(%)',
#  '피부두겹합', '왕복오래달리기출력(VO₂max)', '트레드밀_안정시(bpm)', '트레드밀_3분(bpm)', '트레드밀_6분(bpm)',
#  '트레드밀_9분(bpm)', '트레드밀_계산(VO₂max)', '스텝검사_회복시 심박수(bpm)', '스텝검사_출력(VO₂max)',
#  '허벅지_좌(cm)', '허벅지_우(cm)', '반응시간(초)', '성인체공시간(초)', '사람 운동 처방', 'AI 운동 처방']