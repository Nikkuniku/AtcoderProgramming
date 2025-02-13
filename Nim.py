N = 21
dp = [False] * (N + 1)
for i in range(N + 1):
    if 1 <= i <= 3:
        continue
    for j in range(1, 4):
        if i - j >= 0:
            if not dp[i - j]:
                dp[i] = True
for i in range(N + 1):
    print(i, dp[i])
