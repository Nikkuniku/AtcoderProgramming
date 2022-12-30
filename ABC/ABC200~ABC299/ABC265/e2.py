N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
obstacles = set()
for _ in range(M):
    obstacles.add(tuple(map(int, input().split())))
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
MOD = 998244353
ans = 0

for i in range(N+1):
    for j in range(N+1):
        if i+j > N:
            break
        for k in range(N+1):
            if i+j+k > N:
                break
            now = (A*i+C*j+E*k, B*i+D*j+F*k)
            if now in obstacles:
                continue
            if i-1 >= 0:
                dp[i][j][k] += dp[i-1][j][k]
            if j-1 >= 0:
                dp[i][j][k] += dp[i][j-1][k]
            if k-1 >= 0:
                dp[i][j][k] += dp[i][j][k-1]
            dp[i][j][k] %= MOD

            if i+j+k == N:
                ans += dp[i][j][k]
                ans %= MOD
print(ans)
