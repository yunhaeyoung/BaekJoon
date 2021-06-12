N = int(input()[0])
list = []

x = input().split()

totalY = 0
totalM = 0

# print(x[0])
# print(x[1])
# print(x[2])

for i in range(len(x)):
    totalY += (int(x[i]) // 30 + 1) * 10

#print(totalY)

for i in range(len(x)):
    totalM += (int(x[i]) // 60 + 1) * 15

#print(totalM)

if totalY < totalM:
    print("Y", totalY)
elif totalM < totalY:
    print("M", totalM)
else:
    print("Y", "M", totalY)
