N = int(input())
S = [list(input()) for _ in range(N)]
# 横
ans = "No"
for i in range(N):
    for j in range(N - 5):
        tmp = 0
        for k in range(6):
            tmp += S[i][j + k] == "#"
        if tmp >= 4:
            ans = "Yes"
# 縦
for j in range(N):
    for i in range(N - 5):
        tmp = 0
        for k in range(6):
            tmp += S[i + k][j] == "#"
        if tmp >= 4:
            ans = "Yes"
# 右下方向
for i in range(N - 5):
    for j in range(N - 5):
        tmp = 0
        for k in range(6):
            tmp += S[i + k][j + k] == "#"
        if tmp >= 4:
            ans = "Yes"
# 左下方向
for i in range(N - 5):
    for j in range(5, N):
        tmp = 0
        for k in range(6):
            tmp += S[i + k][j - k] == "#"
        if tmp >= 4:
            ans = "Yes"
print(ans)
