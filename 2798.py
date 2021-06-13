N, M = map(int, input().split())

card = input().split()
card = list(map(int, card))

list = []
ans = 0

for i in range(0, N-2):
    for j in range(i + 1, N-1):
        for k in range(j + 1, N):
            cur = card[i] + card[j] + card[k]
            # if val not in list:
            #     list.append(val)
            if cur == M:
                ans = cur
            elif cur > M:
                continue
            elif cur < M:
                if M - cur < M - ans:
                    ans = cur

print(ans)

# list.sort()

# for i in range(len(list)):
#     if M == list[i]:
#         print(M)
#         break
#     elif list[i] > M:
#         print(list[i - 1])
#         break
    

