H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [A[i][::-1] for i in range(H)]
INF = 1 << 60
ans = 1 << 60
# 左上から右下へ
dp1 = [[INF] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        dp1[i + 1][j + 1] = min(A[i][j], dp1[i][j + 1] + C, dp1[i + 1][j] + C)
for i in range(H):
    for j in range(W):
        tmp = min(dp1[i][j + 1], dp1[i + 1][j]) + C + A[i][j]
        ans = min(ans, tmp)
# 右上から左下へ
dp2 = [[INF] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        dp2[i + 1][j + 1] = min(B[i][j], dp2[i][j + 1] + C, dp2[i + 1][j] + C)
for i in range(H):
    for j in range(W):
        tmp = min(dp2[i][j + 1], dp2[i + 1][j]) + C + B[i][j]
        ans = min(ans, tmp)
print(ans)
