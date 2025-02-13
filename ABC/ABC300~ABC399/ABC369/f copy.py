from bisect import bisect_right, bisect_left

H, W, N = map(int, input().split())

Coins = [list(map(int, input().split())) for _ in range(N)]
Coins.sort(key=lambda x: x[1])
Coins.sort(key=lambda x: x[0])
C = [Coins[i][1] for i in range(N)]
INF = 1 << 60
d = [INF] * (N + 1)
id = [-1] * (N + 1)
prev = [-1] * (N + 1)

for i in range(N):
    j = bisect_right(d, C[i])
    d[j] = C[i]
    id[j] = i
    if j > 0:
        prev[i] = id[j - 1]
m = N - 1
while id[m] == -1:
    m -= 1
path = [(H, W)]
now = id[m]
while now != -1:
    path.append(Coins[now])
    now = prev[now]
path.append((1, 1))
path = path[::-1]
ans = []
for i in range(len(path) - 1):
    d_r = path[i + 1][0] - path[i][0]
    d_c = path[i + 1][1] - path[i][1]
    for _ in range(d_r):
        ans.append("D")
    for _ in range(d_c):
        ans.append("R")
print(len(path) - 2)
print(*ans, sep="")
