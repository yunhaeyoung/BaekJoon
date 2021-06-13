import sys

N = int(input())

list = [0] * 26

for i in range(N):
    str = input()[0]
    list[ord(str) - 97] += 1

flag = 0
ans = ""

for i in range(26):
    if(list[i] >= 5):
        ans = ans + chr(i + 97)
        flag = 1

if flag == 0:
    print("PREDAJA")

if flag == 1:
    print(ans)

