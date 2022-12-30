from itertools import permutations


def candidate(s):
    s = str(s)
    per = permutations(s)
    res = []
    for p in per:
        res.append(int(''.join(p)))
    return res


N, X = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 62
LIM = 10000
dp = [[-INF]*LIM for _ in range(N+1)]
dp[0][X] = 0
kouho = [candidate(i) for i in range(LIM)]
for i in range(N):
    for j in range(LIM):
        if dp[i][j] == -INF:
            continue
        for k in kouho[j]:
            # 買う
            if A[i] <= k:
                dp[i+1][k-A[i]] = max(dp[i+1][k-A[i]], dp[i][j]+1)
            # 買わない
            dp[i+1][k] = max(dp[i+1][k], dp[i][j])

print(max(dp[N]))
