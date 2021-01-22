import sys
sys.stdin = open("input.txt", 'r')

n = input()

for i in range(int(n)):
    str = input().split()
    tmp = float(str[0])
    for j in range(1, len(str)):
        if str[j] == '@':
            tmp *= 3
        elif str[j] == '%':
            tmp += 5
        elif str[j] == '#':
            tmp -= 7
    print(f'{tmp:.2f}')


