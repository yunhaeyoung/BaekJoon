a, b, c, d, e = map(int, input().split())

num = (a ** 2) + (b ** 2) + (c ** 2) + (d ** 2) + (e ** 2)
num = num % 10

print(num)