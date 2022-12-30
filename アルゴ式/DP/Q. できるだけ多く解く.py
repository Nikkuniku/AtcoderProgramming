N = int(input())
T = list(map(int, input().split()))
F = list(map(int, input().split()))
P = [[T[i], F[i]] for i in range(N)]
P.sort(key=lambda x: x[1])
T, F = [P[i][0] for i in range(N)], [P[i][1] for i in range(N)]
F_max = max(F)

dp = [[0]*(F_max+1) for _ in range(N+1)]
for i in range(N):
    ti, fi = T[i], F[i]
    for f in range(F_max+1):
        dp[i+1][f] = max(dp[i+1][f], dp[i][f])
        if 0 <= f+ti <= fi:
            dp[i+1][f+ti] = max(dp[i+1][f+ti], dp[i][f]+1)
print(max(dp[N]))
