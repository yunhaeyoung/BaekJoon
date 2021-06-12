from math import *

P, K = map(int, input().split())

for i in range(5, int(sqrt(P)) + 1, 2):
    if P % i == 0:
        p = i
        q = P // i

if (p > K) & (q > K):
    print("GOOD")
else:
    print("BAD", min(p, q))