from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
cum = defaultdict(int)
cnt = defaultdict(int)
for a in A:
    cum[len(str(a))] += a
    cnt[len(str(a))] += 1
MOD = 998244353
ans = 0
for a in A:
    p = len(str(a))
    for i in range(1, 11):
        ans += (
            cum[i]
            - (a if i == p else 0)
            + a * (cnt[i] - (1 if i == p else 0)) * pow(10, i, MOD)
        )
        ans %= MOD
    cum[p] -= a
    cnt[p] -= 1
print(ans)
