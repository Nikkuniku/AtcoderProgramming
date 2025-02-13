from itertools import pairwise

N = int(input())
A = list(map(int, input().split()))
dp = [[] for _ in range(N)]
dp[-1] = A
for i in range(N - 2, -1, -1):
    B = dp[i + 1]
    for a, b in pairwise(B):
        if i % 2 == 0:
            dp[i].append(max(a, b))
        else:
            dp[i].append(min(a, b))
print(max(dp[0]))
