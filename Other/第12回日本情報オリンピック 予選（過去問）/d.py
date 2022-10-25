d, n = map(int, input().split())
temp = [int(input()) for _ in range(d)]
cloth = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(d+1)]

for i in range(d):
    t = temp[i]
    for j in range(n):
        a, b, c = cloth[j]
        if i == 0:
            if a <= t <= b:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = -1
            continue

        if a <= t <= b:
            for k in range(n):
                _, _, x = cloth[k]
                if dp[i][k] == -1:
                    continue
                dp[i+1][j] = max(dp[i+1][j], dp[i][k]+abs(c-x))
        else:
            dp[i+1][j] = -1

ans = max(dp[d])
print(ans)
