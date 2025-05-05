N, D = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)
C = [0] * (M + 1)
for a in A:
    C[a] += 1
if D == 0:
    ans = sum([max(C[i] - 1, 0) for i in range(M + 1)])
    exit(print(ans))
B = [[] for _ in range(D)]
for v in range(M + 1):
    B[v % D].append(C[v])


def calc(P):
    L = len(P)
    INF = 1 << 60
    dp = [[INF] * 2 for _ in range(L + 1)]
    dp[0] = [0, 0]
    for i in range(L):
        # 取り除く
        dp[i + 1][0] = min(dp[i][0], dp[i][1]) + P[i]
        # 取り除かない
        dp[i + 1][1] = dp[i][0]
    res = min(dp[L])
    return res


ans = 0
for d in range(D):
    ans += calc(B[d])
print(ans)
