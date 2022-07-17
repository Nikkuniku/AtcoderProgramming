dp = [0, 0, 0, 0]
n = int(input())
a = list(map(int, input().split()))
p = 0
for i in range(n):
    dp[0] += 1
    for j in range(3, -1, -1):
        if j+a[i] < 4:
            dp[j+a[i]] = dp[j]
        else:
            p += dp[j]
        dp[j] = 0

print(p)
