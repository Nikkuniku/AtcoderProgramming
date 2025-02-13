def d(P):
    res = 0
    M = len(P)
    for i in range(len(P)):
        res += (2 * i - M + 1) * P[i]
    return res


N = int(input())
P = [[] for _ in range(2)]
for i in range(N):
    x, y = map(int, input().split())
    P[(x + y) % 2].append((i, (x + y) // 2, (x - y) // 2))
ans = 0
for i in range(2):
    for j in [1, 2]:
        ans += d(sorted([P[i][k][j] for k in range(len(P[i]))]))
print(ans)
