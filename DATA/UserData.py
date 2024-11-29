import pandas as pd
import datetime

# 오늘 날짜
today = datetime.date.today().strftime("%y%m%d")

# 유저 데이터 불러오기
df = pd.read_csv("./userdata.csv")
# 유저 숫자 세기
user_count = len(df)

def userProfile(user):
    """
    parameter
    - 입력받은 데이터를 다시 분해하여
    - name, age, height, weight, desease_result = user
    
    return
    - 프롬프트화 한 user data
    """
    name, age, height, weight, desease_result = user
    user = f"""이름 : {name},\n나이 : {age},\n키 : {height},\n몸무게 : {weight},\n보유질환 : {desease_result}"""
    return user

def making_id(today):
    ID = f"{today}-{user_count+1}" # 유저 카운트에서 +1 을 하기
    return ID

# 신규 데이터에 추가
def temp(df, new_user):
    df = df
    name, age, height, weight, desease_result = new_user

    # 새로운 행 데이터
    new_row = {
        "ID":f"{making_id}",
        "NAME": name,
        "측정연령수": age,
        "신장(cm)": height,
        "체중(kg)": weight,
    }

    # 기존 데이터프레임에 행 추가
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("./userdata.csv", index=False)
    return df

# 유저 검색
def searchUser(userdata, id=None, name=None):
    """
    ID와 NAME을 기준으로 데이터를 검색
    
    Parameters:
    - userdata (pd.DataFrame): 사용자 데이터프레임
    - id (str, optional): 검색할 ID
    - name (str, optional): 검색할 이름
    
    Returns:
    - pd.DataFrame: 검색 결과 데이터프레임
    """
    # 검색 조건 초기화
    conditions = []
    
    # ID 조건 추가
    if id:
        conditions.append(userdata["ID"] == id)
    
    # Name 조건 추가
    if name:
        conditions.append(userdata["Name"] == name)
    
    # 조건 조합 (AND 조건)
    if conditions:
        query_result = userdata.loc[pd.concat(conditions, axis=1).all(axis=1)]
    else:
        # 조건이 없으면 전체 데이터 반환
        query_result = userdata
    
    return query_result
    pass

# UserData 불러오기
def Load_user(): 
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