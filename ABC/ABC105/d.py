from collections import defaultdict
n, m = map(int, input().split())
a = list(map(int, input().split()))
csum = [0]
for i in range(n):
    csum.append(csum[-1]+a[i])
d = defaultdict(int)
ans = 0
d[0] = 1
for i in range(1, n+1):
    s = csum[i] % m
    ans += d[s]
    d[s] += 1
print(ans)
