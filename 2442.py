N = int(input())

for i in range(N):
    for j in range(N * 2):
        if (N - 1) - i <= j & j <= (N - 1) + i:
            print("*", end = "")
        elif j < (N - 1) - i:
            print(" ", end = "")
        else:
            print(" ", end = "")
            break
    print("")