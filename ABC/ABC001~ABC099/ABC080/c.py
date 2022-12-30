n = int(input())
F = []
for _ in range(n):
    F.append(tuple(map(int, input().split())))
P = []
for _ in range(n):
    P.append(tuple(map(int, input().split())))
INF = float('inf')
ans = -INF
for i in range(1, 1 << 10):
    store = [0]*n
    for k in range(n):
        for j in range(10):
            if ((i >> j) & 1) and F[k][j] == 1:
                store[k] += 1

    tmp = 0
    for k in range(n):
        tmp += P[k][store[k]]
    ans = max(ans, tmp)
print(ans)
