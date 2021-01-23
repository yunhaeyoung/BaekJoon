import sys
sys.stdin = open("input.txt", 'r')

input = input()
index = input.index(".")

input = input[7:index]
print(input)
new = input[:3]
print(f"{new}{len(input)}{input.count('e')}!")