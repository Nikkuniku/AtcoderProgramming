N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
A.sort()
ans = 0
for a in A:
    ans *= 10
    ans += a
    ans %= MOD
print(ans)
