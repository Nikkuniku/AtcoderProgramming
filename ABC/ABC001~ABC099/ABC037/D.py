from collections import deque
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
Edge = [[] for _ in range(H*W)]
indeg = [0]*H*W
MOD = 10**9 + 7
for i in range(H):
    for j in range(W):
        for dx, dy in dxy:
            ni = i+dx
            nj = j+dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            p = W*i+j
            q = W*ni+nj
            if A[i][j] < A[ni][nj]:
                Edge[p].append(q)
                indeg[q] += 1
q = deque([])
for i, v in enumerate(indeg):
    if v == 0:
        q.append(i)
dp = [[0, 0] for _ in range(H*W)]
seen = [False]*(H*W)
while q:
    v = q.popleft()
    if not seen[v]:
        dp[v][0] += 1
        dp[v][1] += 1
        seen[v] = True
    for e in Edge[v]:
        dp[e][0] += dp[v][0]
        dp[e][1] += dp[v][0]
        dp[e][0] %= MOD
        dp[e][1] %= MOD
        indeg[e] -= 1
        if indeg[e] == 0:
            q.append(e)
ans = sum([dp[i][1] for i in range(H*W)]) % MOD
print(ans)
