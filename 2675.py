import sys
sys.stdin = open("input.txt", 'r')

n = input()

for i in range(int(n)):
    tmp = input().split()
    times = int(tmp[0])
    str = tmp[1]
    new = ""
    for j in range(len(str)):
        for k in range(times):
            new += str[j]
    
    print(new)
