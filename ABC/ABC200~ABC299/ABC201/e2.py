N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append((v, w))
    Edge[v].append((u, w))
MOD = 10**9 + 7
L = 60
dp = [[[0, 0] for _ in range(60)] for _ in range(N)]
ans = 0


def dfs(v, p=-1):
    global ans
    for e, _ in Edge[v]:
        if e == p:
            continue
        dfs(e, v)

    for i in range(L):
        x, y, z = 0, 0, 0
        for e, w in Edge[v]:
            if e == p:
                continue
            if (w >> i) & 1:
                dp[v][i][0] += dp[e][i][1]
                dp[v][i][1] += dp[e][i][0] + 1
                x += dp[e][i][1]
                y += dp[e][i][0] + 1
            else:
                dp[v][i][0] += dp[e][i][0] + 1
                dp[v][i][1] += dp[e][i][1]
                x += dp[e][i][0] + 1
                y += dp[e][i][1]
            z += (dp[e][i][0] + 1) * dp[e][i][1]
        ans += pow(2, i, MOD) * dp[v][i][1]
        ans += pow(2, i, MOD) * (x * y - z)
        ans %= MOD


dfs(0)
print(ans)
