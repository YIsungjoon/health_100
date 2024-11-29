import pandas as pd

def userProfile(name, age, height, weight, desease_result):
    name, age, height, weight, desease_result = name, age, height, weight, desease_result
    user = f"""이름 : {name},\n나이 : {age},\n키 : {height},\n몸무게 : {weight},\n보유질환 : {desease_result}"""
    return user

# 신규 데이터에 추가
def temp():

    pass

# 기존 유저 검색
def temp2():

    pass

# UserData 불러오기
def Load_user():
    df = pd.read_csv("./userdata.csv")
    pass