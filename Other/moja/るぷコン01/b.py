N, X = map(int, input().split())
A = list(map(int, input().split()))
A.append(sum(A))
MOD = 998244353
cum = [0]
for a in A:
    cum.append((cum[-1] + a) % MOD)
for i in range(N + 2, X + 1):
    tmp = (cum[i - 1] - cum[i - 1 - N]) % MOD
    cum.append((cum[-1] + tmp) % MOD)
ans = cum[X] - cum[X - 1]
ans %= MOD
print(ans)
