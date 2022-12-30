A, B = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = list(map(int, input().split()))[::-1]
dp = [[0]*(B+1) for _ in range(A+1)]
S = sum(a)+sum(b)

for i in range(1, A+1):
    if i % 2 == (A+B) % 2:
        dp[i][0] = dp[i-1][0]+a[i-1]
    else:
        dp[i][0] = dp[i-1][0]-a[i-1]
for j in range(1, B+1):
    if j % 2 == (A+B) % 2:
        dp[0][j] = dp[0][j-1]+b[j-1]
    else:
        dp[0][j] = dp[0][j-1]-b[j-1]

for i in range(1, A+1):
    for j in range(1, B+1):
        if (i+j) % 2 == (A+B) % 2:
            dp[i][j] = max(dp[i-1][j]+a[i-1], dp[i][j-1]+b[j-1])
        else:
            dp[i][j] = min(dp[i-1][j]-a[i-1], dp[i][j-1]-b[j-1])
ans = (sum(a)+sum(b)+dp[A][B])//2
print(ans)
