from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))[::-1]
S = SortedList()
ans = 0
MOD = 998244353
for a in A:
    idx = S.bisect_left(a)
    tmp = len(S) - idx
    ans += pow(2, tmp, MOD) - 1
    ans %= MOD
    S.add(a)
print(ans)
