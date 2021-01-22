import sys
sys.stdin = open("input.txt", 'r')

while True:
    tmp = input().split()

    m = int(tmp[0])
    f = int(tmp[1])

    if m == 0 and f == 0:
        break;

    print(m+f)


