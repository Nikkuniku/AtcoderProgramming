from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
ans = 1
MOD = 1000000007
d = defaultdict(int)
d[-1] = 3
for a in A:
    ans *= d[a - 1] - d[a]
    ans %= MOD
    d[a] += 1
print(ans)
