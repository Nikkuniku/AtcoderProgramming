from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]
INF = 10**18
dp = [INF]*(n+1)

for i in range(n):
    idx = bisect_left(dp, a[i])
    dp[idx] = min(dp[idx], a[i])

ans=0
for i in dp:
    if i==INF:
        break
    ans+=1
print(ans)
    