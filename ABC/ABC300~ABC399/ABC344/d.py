T = " " + input()
N = int(input())
S = [list(input().split()) for _ in range(N)]
INF = 1 << 60
dp = [[INF] * (len(T)) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    A = int(S[i][0])
    B = S[i][1:]
    for j in range(len(T)):
        if dp[i][j] == INF:
            continue
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        for s in B:
            M = len(s)
            isOK = True
            for k in range(M):
                if j + 1 + k > len(T) - 1:
                    isOK = False
                    continue
                if T[j + 1 + k] != s[k]:
                    isOK = False
            if isOK:
                dp[i + 1][j + M] = min(dp[i + 1][j + M], dp[i][j] + 1)
ans = dp[N][len(T) - 1]
if ans == INF:
    ans = -1
print(ans)
