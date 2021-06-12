N = int(input())

for i in range(2 * N):
    for j in range(2 * N - 1):
        if i <= 4:
            if (N - 1) - i <= j <= (N - 1) + i:
                print("*", end = "")
            elif j < (N - 1) - i:
                print(" ", end = "")
            else:
                print(" ", end = "")
                break
        print("")
        else:
            if (N - 1) - (i - 2) <= j <= (N - 1) + (i - 2):
                print("*", end = "")
            elif j < (N - 1) - (i - 2):
                print(" ", end = "")
            else:
                print(" ", end = "")
                break
            print("")