# Quiz 3

# url = "http://google.com"

# url = url[7:]
# # url = url.replace("http://", "")
# url = url[:-4]
# # url = url[:url.index(".")]

# ans = url[:3] + "" + str(len(url)) + "" + str(url.count('e')) + "!"

# print("{0}의 비밀번호는 {1}입니다.".format(url, ans))

# 리스트
# subway = [10, 20, 30]
# print(subway)

# subway = ["고양이", "햄스터", "강아지"]
# print(subway)

# print(subway.index("햄스터"))

# subway.append("거북이") #append : 계속 끝에 붙이기
# print(subway)

# subway.insert(1, "물고기") #insert : 원하는 인덱스에 삽입
# print(subway)

# print(subway.pop()) #pop : 마지막 요소 삭제
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.count("햄스터"))

# num_list = [4, 9, 3, 6, 1]
# num_list.sort() #sort : 리스트 정렬
# print(num_list)

# num_list.reverse() #reverse : 역순으로 수정
# print(num_list)

# num_list.clear() #clear : 전체 삭제
# print(num_list)

# num_list = [3, 9, 2, 1, 0]
# mix_list = ["하이", 99, True]

# num_list.extend(mix_list) #extend : 리스트끼리 이어붙이기
# print(num_list)

# 사전
# key = {3 : "햄스터", 100 : "고양이"} #1:1매치
# print(key[3])
# print(key[100])

# print(key.get(3))
# print(key.get(100))

# # print(key[9]) #key[9] : 없는 값을 받아 올 경우 프로그램 종료
# # print(key.get(9)) # get함수 이용시 None출력 후 정상 작동
# print(key.get(9, "아무도 없어서 사용가능합니닷")) #없다면 출력~
# print("hi")

# print(3 in key) #in을 이용해 사전에서 있없 체크!
# print(9 in key)

# key = {"C20" : "햄스터", "A28" : "고양이"} #1:1매치
# print(key["C20"])
# print(key.get("C20"))

# key["C20"] = "물고기"
# print(key["C20"])

# key["D90"] = "도롱뇽"
# print(key)

# del key["A28"] #값 삭제 앞에 del!
# print(key)

# print(key.keys()) #key만 출력 (앞에 꺼)
# print(key.values()) #value만 출력 (뒤에 꺼)

# print(key.items()) #key,value 쌍으로 출력! items

# key.clear() #모두 삭제 clear
# print(key)

#1:40:46