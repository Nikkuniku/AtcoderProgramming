N, Q = map(int, input().split())
U, V = [], []
P = []
for _ in range(N):
    x, y = map(int, input().split())
    U.append(x + y)
    V.append(x - y)
    P.append((x, y))
U.sort()
V.sort()
ans = []
for _ in range(Q):
    q = int(input())
    x, y = P[q - 1]
    u = x + y
    v = x - y
    res = []
    for i in [0, -1]:
        res.append(abs(u - U[i]))
        res.append(abs(v - V[i]))
    ans.append(max(res))
print(*ans, sep="\n")
