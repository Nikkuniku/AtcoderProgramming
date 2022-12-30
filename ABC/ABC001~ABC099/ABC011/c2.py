N = int(input())
NGs = set(int(input()) for _ in range(3))
INF = 1 << 10
dp = [INF]*(N+1)
dp[0] = 0
for i in range(N):
    for j in range(1, 4):
        if i+j not in NGs:
            if i+j > N:
                continue
            dp[i+j] = min(dp[i+j], dp[i]+1)
ans = 'NO'
if dp[N] <= 100:
    ans = 'YES'
print(ans)
