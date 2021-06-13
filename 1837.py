from math import *

P, K = map(int, input().split())

list = [1] * K
print(list)
# 소수 판별
# for i in range(5, int(sqrt(P)) + 1, 2):
#     if P % i == 0:
#         p = i
#         q = P // i

# 에라토스테네스의 체


# if (p > K) & (q > K):
#     print("GOOD")
# else:
#     print("BAD", min(p, q))