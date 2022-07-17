from operator import ne


m, n = map(int, input().split())
MOD = 10**9 + 7

next = [1]*31
for i in range(30):
    next[i] = m % MOD
    m *= m
    m %= MOD

ans = 1
for i in range(30):
    if n & (1 << i):
        ans *= next[i]
        ans %= MOD
print(ans)
