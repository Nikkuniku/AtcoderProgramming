from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i, v in enumerate(A):
    d[v] = i + 1
now = d[-1]
ans = []
while len(ans) < N:
    ans.append(now)
    now = d[now]
print(*ans)
