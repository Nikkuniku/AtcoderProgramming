N, M, D, K = map(int, input().split())
Edge = []
for i in range(M):
    u, v, w = map(int, input().split())
    Edge.append((i, u, v, w))

for _ in range(N):
    x, y = map(int, input().split())

Edge.sort(key=lambda x: x[3])
ans = [-1]*M
now = -1
for i in range(D):
    for _ in range(K):
        now += 1
        if now > M-1:
            break
        ans[Edge[now][0]] = i+1
print(*ans)
