###################################
# 1. 화씨 -> 섭씨 변환
# 2. Celcious = (F - 32) / 1.8
###################################

def celcious_to_fahrenhiet(F):
    return ((F - 32) / 1.8)

print("77도 화씨는 섭씨로")
print(celcious_to_fahrenhiet(77))
print("도(섭씨) 입니다.")
