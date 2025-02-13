from collections import defaultdict

d = defaultdict(int)
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += d[i - A[i]]
    d[i + A[i]] += 1
print(ans)
