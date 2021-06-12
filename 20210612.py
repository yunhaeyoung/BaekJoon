#숫자 출력 
# print(5)
# print(-10)
# print(3.14)
# print(5+3)
# print(8*8)
# print(3*(3+1))

#문자열 출력
# print('작은 따옴표')
# print("큰 따옴표")
# print("오에"*10)

#boolean
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not (5 > 3))

#변수
# animal = "고양이"
# name = "땅콩스"
# age = 1.5
# hobby = "사냥"
# is_adult = age >= 1

# print(animal + "이름은" + name)
# print(name + "는 " + str(age) + "살이고 " + hobby + "를 매우 좋아함")
# print(name, "는 ", age, "살이고 ", hobby, "를 매우 좋아함")
# print(name + "는 성묘냐? " + str(is_adult))

 #str()함수를 사용하지 않는 방법 -> , 쓰기!
#문자열을 제외하고는 모두 str으로 바꿔줘야함

#주석
'''나아아아아
아아아아
아아아아
아아아아'''
#여러 줄 쓰기 -> 작은 따옴표 세번!!!

#Quiz 1
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

#연산자
# print(1+1)
# print(4-1)
# print(5*8)
# print(8/4)

# print(2**3) #2^3
# print(5%4) #나머지
# print(5//4) #몫

# print(10 > 5)
# print(5 <= 7)
# print(10 < 2)

# print(1 == 1)
# print(5 + 4 == 9)
# print(5 != 9)
# print(not (5 == 9))

# print((3 > 0) and (3 < 5))
# print((3 < 0) and (3 < 5))
# print((3 > 0) & (3 < 5))

# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))

# print(5 > 4 > 3)
# print(5 > 4 > 9)

#수식
# print(2 + 3 * 4)
# print((2 + 3) * 4)
# number = 2 + 3 * 4
# print(number)
# number += 2
# print(number)
# number -= 10
# print(number)

# number %= 4
# print(number)

# 숫자 처리 함수
# print(abs(-5)) #절대값
# print(pow(4, 2)) #4^2
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14)) #반올림
# print(round(4.6))

# from math import *
# print(floor(4.99)) #내림
# print(ceil(4.11)) #올림
# print(sqrt(16)) #제곱근

# 랜덤 함수
# from random import *

# print(random()) # 0.0 ~ 1.0 미만의 랜덤 값
# print(random() * 100) # 0.0 ~ 100.0 미만의 랜덤 값
# print(int(random() * 100))
# print(int(random() * 100) + 1) # 1 ~ 100 이하의 랜덤 값

# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46)) # 1 ~ 46 미만의 랜덤 값
# print(randint(1, 45)) # 1 ~ 45 이하의 랜덤 값

# Quiz 2
# from random import *

# date = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")

# 문자열
# sentence1 = '나는 멋지다'
# print(sentence1)
# sentence2 = "나는 멋지다"
# print(sentence2)

# sentence3 = """
# 나는 멋지고
# 나는 멋지다
# """
# print(sentence3)

# 슬라이싱
# personalInfo = "981014-2345678"
# print("성별 : " + personalInfo[7])
# print("년도 : " + personalInfo[0:2]) # 0 ~ 2 이전까지
# print("월 : " + personalInfo[2:4])
# print("일 : " + personalInfo[4:6])

# print("생년월일 : " + personalInfo[:6]) # == 0:6
# print("뒤 7자리 : " + personalInfo[7:]) # == 7:끝
# print("뒤 7자리(뒤에서 부터) : " + personalInfo[-7:]) #맨 뒤에서 7번째:끝

# 문자열 처리 함수 55:09