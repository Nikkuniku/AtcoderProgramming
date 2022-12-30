from collections import defaultdict
H, W, N, h, w = map(int, input().split())
A = [[0]*(W+1)]
for _ in range(H):
    A.append([0]+list(map(int, input().split())))
d = defaultdict(int)
cumsum = [[[0]*(W+1) for _ in range(H+1)] for _ in range(N+1)]

for i in range(H+1):
    for j in range(W+1):
        d[A[i][j]] += 1
        cumsum[A[i][j]][i][j] += 1

for k in range(N+1):
    for i in range(H+1):
        for j in range(1, W+1):
            cumsum[k][i][j] += cumsum[k][i][j-1]
for k in range(N+1):
    for j in range(W+1):
        for i in range(1, H+1):
            cumsum[k][i][j] += cumsum[k][i-1][j]
ans = [[0]*(W-w+1) for _ in range(H-h+1)]

for k in range(1, N+1):
    for i in range(1, H-h+2):
        for j in range(1, W-w+2):
            # 長方形内のkの個数
            tmp = cumsum[k][i+h-1][j+w-1]-cumsum[k][i-1][j+w-1] - \
                cumsum[k][i+h-1][j-1]+cumsum[k][i-1][j-1]
            ans[i-1][j-1] += 1 if d[k]-tmp >= 1 else 0

for a in ans:
    print(*a)
