n, x = map(int, input().split())
a = list(map(int, input().split()))
dp = [-1]*(n+1)
cum = [0]
dp[0] = 0
for p in a:
    cum.append(cum[-1]+p)
for i in range(n):
    for j in range(i+1):
        if dp[j] != -1 and cum[i+1]-cum[j] >= x:
            dp[i+1] = max(dp[i+1], dp[j]+1)

print(dp[n])
