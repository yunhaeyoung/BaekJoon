ans = ""

while True:
    sentence = input().lower()

    if sentence == "#":
        break

    idx = 0
    cnt = 0

    while True:
        idx = sentence.find(sentence[0], idx + 1)
        if idx == -1:
            break
        cnt += 1

    ans += sentence[0] + " " + str(cnt) + "\n"
print(ans[:-1])
