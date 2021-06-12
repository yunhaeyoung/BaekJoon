N = int(input())

for i in range(N):
    for j in range(2 * N - 1):
        if i <= j <= (2 * N - 2) - i:
            print("*", end = "")
        elif j < i:
            print(" ", end = "")
        else:
            print(" ", end = "")
            break
    print("")