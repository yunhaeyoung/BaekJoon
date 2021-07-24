T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    #print("k : ", k, " n : ", n)

    for j in range(1, k-1, 1):
        arr = [[1, 2, 3]]
        arr[j].append(arr[0][0], arr[0][1], arr[0][2])

