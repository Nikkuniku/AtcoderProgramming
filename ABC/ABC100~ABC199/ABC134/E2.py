from bisect import bisect_right, bisect_left
N = int(input())
A = [int(input()) for _ in range(N)][::-1]
INF = 1 << 62
dp = [INF]*(N+1)
for a in A:
    idx = bisect_right(dp, a)
    dp[idx] = a
ans = bisect_left(dp, INF)
print(ans)
