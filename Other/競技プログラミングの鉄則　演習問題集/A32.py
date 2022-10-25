n, a, b = map(int, input().split())
dp = [False]*(n+1)
for i in range(0, n+1):
    if i-a >= 0:
        dp[i] |= not dp[i-a]
    if i-b >= 0:
        dp[i] |= not dp[i-b]
ans = 'Second'
if dp[n]:
    ans = 'First'
print(ans)
