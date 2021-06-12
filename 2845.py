num, area = map(int, input().split())
a, b, c, d, e = map(int, input().split())

total = num * area

print((a - total), (b - total), (c - total), (d - total), (e - total))
