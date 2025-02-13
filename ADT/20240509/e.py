N = int(input())
S = [list(input()) for _ in range(N)]
ans = "No"
# 上
for i in range(N):
    if i + 5 > N - 1:
        break
    for j in range(N):
        w, b = 0, 0
        for k in range(i, i + 6):
            if S[k][j] == ".":
                w += 1
            else:
                b += 1
        if w <= 2:
            ans = "Yes"
for i in range(N):
    for j in range(N):
        if j + 5 > N - 1:
            break
        w, b = 0, 0
        for k in range(j, j + 6):
            if S[i][k] == ".":
                w += 1
            else:
                b += 1
        if w <= 2:
            ans = "Yes"
for i in range(N):
    if i + 5 > N - 1:
        continue
    for j in range(N):
        if j + 5 > N - 1:
            continue
        w, b = 0, 0
        for k in range(6):
            if S[i + k][j + k] == ".":
                w += 1
            else:
                b += 1
        if w <= 2:
            ans = "Yes"
for i in range(N):
    if i + 5 > N - 1:
        continue
    for j in range(N):
        if j - 5 < 0:
            continue
        w, b = 0, 0
        for k in range(6):
            if S[i + k][j - k] == ".":
                w += 1
            else:
                b += 1
        if w <= 2:
            ans = "Yes"
print(ans)
