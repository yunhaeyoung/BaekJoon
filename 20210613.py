# 문자열 처리 함수
# line = "Hi This is Haeyoung"
# print(line)
# print(line.lower()) #소문자 변환
# print(line.upper()) #대문자 변환

# print(line[0].isupper()) #대문자인지 검사
# print(len(line)) #문자열 길이
# print(line.replace("This", "She")) #교체

# idx = line.index("i") #첫번째만 알려줌
# print(idx)

# idx = line.index("i", idx + 1) #또 찾아봐
# print(idx)

# print(line.find("That")) #원하는 값이 없을 경우 -1리턴
# #print(line.index("That")) #얘는 아예 에러남

# print(line.count("i")) #문자열에서 i가 총 몇 번 나타나는지

#문자열 포맷
# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d살입니다." % 24)
# print("나는 %s를 좋아해요" % "파이썬")
# print("Apple은 %c로 시작한다~" % "A")

# print("나는 %s살입니다." % 24) # 정수 -> 문자열
# print("나는 %s색이랑 %s색 좋아함 ~" % ("하늘", "노랑"))

# 방법 2
# print("나는 {}살이다 ~ ".format(20))
# print("나는 {}색이랑 {}색 좋아함 ~".format("하늘", "노랑"))
# print("나는 {0}색이랑 {1}색 좋아함 ~".format("하늘", "노랑"))
# print("나는 {1}색이랑 {0}색 좋아함 ~".format("하늘", "노랑"))

# 방법 3
# print("나는 {age}살이고, {movie}영화를 좋아한다 ~ ".format(age = 24, movie = "Baby Driver"))
# print("나는 {age}살이고, {movie}영화를 좋아한다 ~ ".format(movie = "Baby Driver", age = 24))

# 방법 4
# age = 30
# movie = "Disney"
# print(f"나는 {age}살이고, {movie}영화를 좋아한다 ~ ")

#탈출 문자
# print("요로시꾸\n오네가이시마스")

# print('하이 "나다!"')
# print("하이 \"나다!\"") #큰 따옴표 안 큰 따옴표 출력하기

# \\ : 문장 속에선 \
# print("하\\이\\안\\녕\\하\\세\\요")

# \r : 커서를 맨 앞으로 이동
print("Red  Apple\rPine") #커서를 맨 앞으로 이동해서 겹쳐쓰기

# \b : 백스페이스 (한 글자 삭제)
print("Redd \bApple")