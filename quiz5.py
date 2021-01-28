# from random import *

# list = []
# total = 0

# for customer in range(1, 51):
#     randTime = randint(5, 51) #5~50
#     list.append(randTime)

# for i in range(0, 50): #리스트 끝까지는 어떻게?
#     if 5 <= list[i] and list[i] <= 15:
#         total += 1

# for i in range(0, 50):
#     print("{0}번째 손님 (소요시간 : {1}분)".format(i+1, list[i]))
# print("총 탑승 승객 : {0}".format(total))
    
# from random import *
# cnt = 0
# for i in range(1, 51): #1~50
#     time = randrange(5, 51) #5~50
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))