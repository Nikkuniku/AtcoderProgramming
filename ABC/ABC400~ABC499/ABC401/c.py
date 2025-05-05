from itertools import accumulate

N, K = map(int, input().split())
A = []
MOD = 1000000000
for i in range(K):
    A.append(1)
cum = list(accumulate(A, initial=0))
for i in range(K, N + 1):
    temp = cum[-1] - cum[i - K]
    temp %= MOD
    A.append(temp)
    cum.append((temp + cum[-1]) % MOD)
print(A[-1])
