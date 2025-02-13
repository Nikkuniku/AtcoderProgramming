N = int(input())
S = 0
P = []
for _ in range(N):
    A, B = map(int, input().split())
    S += B
    P.append((A, B))
if S % 3 != 0:
    exit(print(-1))
X = S // 3
INF = 1e18
dp = [[[INF] * (X + 1) for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    a, b = P[i]
    for s in range(X + 1):
        for t in range(X + 1):
            if a == 1:
                if s + b <= X:
                    dp[i + 1][s + b][t] = min(dp[i + 1][s + b][t], dp[i][s][t])
                if t + b <= X:
                    dp[i + 1][s][t + b] = min(dp[i + 1][s][t + b], dp[i][s][t] + 1)
                dp[i + 1][s][t] = min(dp[i + 1][s][t], dp[i][s][t] + 1)
            elif a == 2:
                if s + b <= X:
                    dp[i + 1][s + b][t] = min(dp[i + 1][s + b][t], dp[i][s][t] + 1)
                if t + b <= X:
                    dp[i + 1][s][t + b] = min(dp[i + 1][s][t + b], dp[i][s][t])
                dp[i + 1][s][t] = min(dp[i + 1][s][t], dp[i][s][t] + 1)
            elif a == 3:
                if s + b <= X:
                    dp[i + 1][s + b][t] = min(dp[i + 1][s + b][t], dp[i][s][t] + 1)
                if t + b <= X:
                    dp[i + 1][s][t + b] = min(dp[i + 1][s][t + b], dp[i][s][t] + 1)
                dp[i + 1][s][t] = min(dp[i + 1][s][t], dp[i][s][t])
ans = dp[N][X][X]
if ans == INF:
    ans = -1
print(ans)
