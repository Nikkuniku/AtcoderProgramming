from itertools import accumulate
from collections import defaultdict
from random import randint

R = randint(1, 1 << 60)
N, K = map(int, input().split())
A = list(map(int, input().split()))
cum = list(accumulate(A, initial=0))
dp = [0] * (N + 1)
dp[0] = 1
MOD = 998244353
d = defaultdict(int)
d[0 ^ R] = 1
S = 1
for i in range(N):
    dp[i + 1] = S - d[(cum[i + 1] - K) ^ R]
    dp[i + 1] %= MOD
    S += dp[i + 1]
    d[cum[i + 1] ^ R] += dp[i + 1]

print(pow(2, N - 1) - dp[-1])
