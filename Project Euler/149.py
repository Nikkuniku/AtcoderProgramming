def f(A):
    minval = 0
    cum = 0
    res = -(1 << 60)
    for a in A:
        cum += a
        res = max(res, cum - minval)
        minval = min(minval, cum)
    return res


C = 500000
MOD = 1000000
s = [
    (100003 - 200003 * (k + 1) + 300007 * (k + 1) * (k + 1) * (k + 1)) % MOD - C
    for k in range(55)
]
for k in range(55, 4000000 + 1):
    temp = (s[k - 24] + s[k - 55] + 1000000) % MOD - C
    s.append(temp)
N = 2000
T = [[] for _ in range(N)]
for i in range(N * N):
    T[i // N].append(s[i])
ans = -(1 << 60)
# 横
for i in range(N):
    ans = max(ans, f(T[i]))
# 縦
for j in range(N):
    cols = [T[i][j] for i in range(N)]
    ans = max(ans, f(cols))
# 右下
for j in range(N):
    vals = []
    dx, dy = 1, 1
    nx, ny = 0, j
    while nx < N and ny < N:
        vals.append(T[nx][ny])
        nx += dx
        ny += dy
    ans = max(ans, f(vals))
for i in range(N):
    vals = []
    dx, dy = 1, 1
    nx, ny = i, 0
    while nx < N and ny < N:
        vals.append(T[nx][ny])
        nx += dx
        ny += dy
    ans = max(ans, f(vals))
# 左下
for j in range(N):
    vals = []
    dx, dy = 1, -1
    nx, ny = 0, j
    while nx < N and ny < N:
        vals.append(T[nx][ny])
        nx += dx
        ny += dy
    ans = max(ans, f(vals))
for i in range(N):
    vals = []
    dx, dy = 1, -1
    nx, ny = i, N - 1
    while nx < N and ny < N:
        vals.append(T[nx][ny])
        nx += dx
        ny += dy
    ans = max(ans, f(vals))
print(ans)
