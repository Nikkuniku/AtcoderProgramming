from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
ans = 0
for i in range(N):
    ans += d[i + 1 - A[i]]
    d[i + 1 + A[i]] += 1
print(ans)
