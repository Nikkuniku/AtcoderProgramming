n = int(input())
s = [int(input()) for _ in range(n)]
dp = [[False]*(sum(s)+2) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(sum(s)+2):
        dp[i+1][j] |= dp[i][j]
        if j-s[i] >= 0:
            dp[i+1][j] |= dp[i][j-s[i]]

ans = [0]
for j in range(sum(s)+2):
    if dp[n][j] and j % 10 != 0:
        ans.append(j)
print(max(ans))
