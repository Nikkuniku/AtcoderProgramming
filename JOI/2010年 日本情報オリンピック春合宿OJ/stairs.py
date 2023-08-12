from bisect import bisect_left as bl
from itertools import accumulate
N, P = map(int, input().split())
H = [int(input()) for _ in range(N)]
dp = [0]*(N+1)
dp[0] = 1
MOD = 1234567
H = list(accumulate([0]+H))
for i in range(1, N+1):
    h = H[i]
    q = h-P
    j = bl(H, q)
    if j == 0:
        dp[i] = dp[i-1] % MOD
    else:
        dp[i] = (dp[i-1]-dp[j-1]) % MOD
    if i == N:
        break
    dp[i] += dp[i-1]
    dp[i] %= MOD
ans = dp[-1] % MOD
print(ans)
