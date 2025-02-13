H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]
yoko_maru = [[0] * (W + 1) for _ in range(H + 1)]
yoko_batsu = [[0] * (W + 1) for _ in range(H + 1)]
yoko_blank = [[0] * (W + 1) for _ in range(H + 1)]
tate_maru = [[0] * (H + 1) for _ in range(W + 1)]
tate_batsu = [[0] * (H + 1) for _ in range(W + 1)]
tate_blank = [[0] * (H + 1) for _ in range(W + 1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            yoko_maru[i + 1][j + 1] += 1
            tate_maru[j + 1][i + 1] += 1
        elif S[i][j] == "x":
            yoko_batsu[i + 1][j + 1] += 1
            tate_batsu[j + 1][i + 1] += 1
        else:
            yoko_blank[i + 1][j + 1] += 1
            tate_blank[j + 1][i + 1] += 1
# 累積
for i in range(H + 1):
    for j in range(W):
        yoko_maru[i][j + 1] += yoko_maru[i][j]
        yoko_batsu[i][j + 1] += yoko_batsu[i][j]
        yoko_blank[i][j + 1] += yoko_blank[i][j]
for j in range(W + 1):
    for i in range(H):
        tate_maru[j][i + 1] += tate_maru[j][i]
        tate_batsu[j][i + 1] += tate_batsu[j][i]
        tate_blank[j][i + 1] += tate_blank[j][i]
INF = 1 << 60
ans = INF
for i in range(H):
    for j in range(W):
        if j + K <= W:
            tmp_yoko = yoko_maru[i + 1][j + K] - yoko_maru[i + 1][j]
            blank_yoko = yoko_blank[i + 1][j + K] - yoko_blank[i + 1][j]
            batsu_yoko = yoko_batsu[i + 1][j + K] - yoko_batsu[i + 1][j]
            if tmp_yoko + blank_yoko == K and batsu_yoko == 0:
                ans = min(ans, blank_yoko)
        if i + K <= H:
            tmp_maru = tate_maru[j + 1][i + K] - tate_maru[j + 1][i]
            blank_tate = tate_blank[j + 1][i + K] - tate_blank[j + 1][i]
            batsu_tate = tate_batsu[j + 1][i + K] - tate_batsu[j + 1][i]
            if tmp_maru + blank_tate == K and batsu_tate == 0:
                ans = min(ans, blank_tate)
if ans == INF:
    ans = -1
print(ans)
