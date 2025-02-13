N, A, B = map(int, input().split())
dp = [False] * (N + 1)
for x in range(N + 1):
    isWin = False
    if x - A >= 0 and not dp[x - A]:
        isWin = True
    if x - B >= 0 and not dp[x - B]:
        isWin = True
    dp[x] = isWin
ans = "First" if dp[N] else "Second"
print(ans)
