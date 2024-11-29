

def userProfile(name, age, height, weight, desease_result):
    name, age, height, weight, desease_result = name, age, height, weight, desease_result
    user = f"""이름 : {name},\n나이 : {age},\n키 : {height},\n몸무게 : {weight},\n보유질환 : {desease_result}"""
    return user