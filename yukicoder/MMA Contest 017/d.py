N = int(input())
A = list(map(int, input().split()))
ans = 0
MOD = 998244353
cum=1
for i in range(N):
    ans+=
    ans += (pow(2, i + 1, MOD) - 1) * A[i] % MOD
    ans %= MOD
print(ans)
