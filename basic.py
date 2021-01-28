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

# cabinet = {"A-3":"유재석", "B-100":"조세호"}
# print(cabinet[3])
# print(cabinet[100]) 

# print(cabinet.get(3))
# print(cabinet[5]) #오류발생 & 프로그램 종료
# print(cabinet.get(5)) #none출력
# print(cabinet.get(5, "비었다"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# print(cabinet["A-3"])
# print(cabinet["B-100"])

#insert
# print(cabinet)
# cabinet["C-29"] = "김태호"
# cabinet["A-10"] = "윤효전"
# print(cabinet)

# #delete
# del cabinet["C-29"]
# print(cabinet)

#key만 출력하기
# print(cabinet.keys())

#value만 출력하기
# print(cabinet.values())

#(key, value)쌍으로 출력하기
# print(cabinet.items())

#clear
# cabinet.clear()
# print(cabinet)

#<튜플> - 변경되지 않는 리스트
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") #추가 불가

# name = "김종국"
# age = 29
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

#<세트> - 중복X, 순서X
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"윤효전", "김태호", "조세호"}
# python = set(["윤효전", "윤혜영"])

#교집합
# print(java & python)
# print(java.intersection(python))

#합집합
# print(java | python)
# print(java.union(python))

#차집합
# print(java - python)
# print(java.difference(python))

# print(python)
# python.add("김태호")
# print(python)

# python.remove("김태호")
# print(python)

#자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # set {}
  
# menu = list(menu)
# print(menu, type(menu)) # list []

# menu = tuple(menu) 
# print(menu, type(menu)) # tuple ()

# menu = set(menu)
# print(menu, type(menu)) # set

# if
# weather = input("날씨 어때? ")
# if weather == "비" or weather == "눈":
#     print("우산 챙기셈")
# elif weather == "미세먼지":
#     print("마스크 챙기셈")
# else:
#     print("준비물 필요없음")

# temp = int(input("기온 어때? "))
# if 30 <= temp:
#     print("너무 덥다")
# elif 10 <= temp and temp < 30:
#     print("날씨 괜춘")
# elif 0 <= temp and temp < 10:
#     print("외투 챙기셈")
# else:
#     print("너무 춥다")

#2:05:08

# for
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기 번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6): #1, 2, 3, 4, 5
#     print("대기 번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피 준비됨. {1}번 남았다".format(customer, index))
#     index -= 1
# if index == 0:
#     print("커피 폐기")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피 준비됨. {1}번 호출".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피 준비됨".format(customer))
#     person = input("이름 ? ")

# absent = [2, 5] #결석
# no_book = [7]
# for student in range(1, 11): #1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 끝, {0} 때문임".format(student))
#         break
#     print("{0} 책 읽어라".format(student))

# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["IronMan", "Thor", "IAmGroot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# students = ["IronMan", "Thor", "IAmGroot"]
# print(students)
# students = [i.upper() for i in students]
# print(students)

# 함수
# def open_account():
#     print("새로운 계좌가 생성됨")

# def deposit(balance, money): #입금
#     print("입금 완료. 잔액 : {0} 원".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print("출금 완료. 잔액은 {0} 원".format(balance - money))
#         return balance - money
#     else:
#         print("출금 불가. 잔액은 {0} 원".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# balance = deposit(balance, 500)

# balance = withdraw(balance, 300)
# balance = withdraw(balance, 10000)

# commission, balance = withdraw_night(balance, 500)
# print("수수료 : {0} 원\t잔액 : {1} 원".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("윤효전", 29, "Python")
# profile("윤혜영", 24, "Java")

# 기본값
# def profile(name, age = 20, main_lang = "C"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("윤효전")
# profile("윤혜영")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "Python", age = 20)
profile(main_lang = "Java", age = 29, name = "김태호")