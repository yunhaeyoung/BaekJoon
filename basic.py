# from random import *

# print(random()) # 0.0 ~ 1.0 미만 랜덤값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 사이 랜덤값

# print(int(random() * 45) + 1) #1 ~ 45
# print(randrange(1, 46))
# print(randint(1, 45))

# print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + " 일로 선정되었습니다.")

# sentence = '나는 효전입니다'
# print(sentence)
# sentence2 = "효전이는 귀엽다"
# print(sentence2)
# sentence3 = """
# 나는 효전이고,
# 효전이는 귀여워요
# """
# print(sentence3)

# regNum = "930104-1392033"

# print("성별 : " + regNum[7])
# print("연 : " + regNum[0:2]) # 0 ~ 1
# print("월 : " + regNum[2:4])
# print("일 : " + regNum[4:6])

# print("생년월일 : " + regNum[:6]) #처음부터
# print("뒤 7자리 : " + regNum[7:])  #7부터 끝까지
# print("뒤 7자리 (뒤부터 읽기) : " + regNum[-7:]) #맨 뒤의 7번째부터 끝까지

# hyojeon = "Hyojeon is Cute"
# print(hyojeon.lower())
# print(hyojeon.upper())
# print(hyojeon[0].isupper())
# print(len(hyojeon))
# print(hyojeon.replace("Hyojeon", "Haeyoung"))

# index = hyojeon.index("e")
# print(index)
# index = hyojeon.index("e", index + 1)
# print(index)

# print(hyojeon.find("Haeyong")) #-1 리턴
# # print(hyojeon.index("Haeyoung")) #오류

# print(hyojeon.count("e"))

##방법1
# print("A" + "B")
# print("A", "b")

# print("나는 %d살 입니다." % 24)
# print(f"나는 {'!_3'}살입니다.")
# print("나는 %s를 좋아해." %"효전이")
# print("Apple은 %c로 시작해." %"A")
# print("나는 %s색 %s색" %("효전", "효전"))

##방법2
# print("나는 {}살입니다.".format(24))
# print("나는 {}색과 {}색을 좋아해".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해".format("파란", "빨간"))

##방법3
# print("나는 {age}살이며 {color}색을 좋아해".format(age = 24, color = "Blue"))
# print("나는 {age}살이며 {color}색을 좋아해".format(color = "Blue", age = 24))

##방법4
# age = 24
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해")

#\n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# #\" \' : 문장 내에서 따옴표
# print("저는'윤혜영'입니다")
# print('저는"윤혜영"입니다')
# print("저는 \"윤혜영\"입니다")
# print("저는 \'윤혜영\'입니다")

# # \\ : 문장 내에서 \
# print("C:\\Users\\haeyo\\Desktop\\BaekJoon>")

# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") #PineApple

# #\b : 백스페이스(한 글자 지우기)
# print("Redd\bApple")

# #\t : 탭
# print("Red\tApple")

# 리스트[]
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "혜영"]
# print(subway)

# print(subway.index("혜영"))

# # 효전 탑승
# subway.append("효전")
# print(subway)

# # 땅콩 유재석 / 조세호 사이 탑승
# subway.insert(1, "땅콩")
# print(subway)

# # # 뒤에서부터 한명씩 제거
# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름 찾기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# num_list = [5, 3, 2, 1, 4]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 가능
# mix_list = ["조세호", 20, True]
# num_list = [5, 3, 2, 1, 4]
# print(mix_list)

# # 리스트 합치기
# num_list.extend(mix_list)
# print(num_list)

# 1:31:36