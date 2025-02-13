N = 1000
ans = 0
MOD = 10000000000
for i in range(1, N + 1):
    ans += pow(i, i, MOD)
    ans %= MOD
print(ans)
