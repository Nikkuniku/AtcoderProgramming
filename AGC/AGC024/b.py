from collections import defaultdict
d = defaultdict(int)

n = int(input())
p = [int(input()) for _ in range(n)]

for i in range(n):
    d[p[i]] = d[p[i]-1]+1

ans = n-max(d.values())
print(ans)
