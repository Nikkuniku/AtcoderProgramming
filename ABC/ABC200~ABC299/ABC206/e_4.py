L, R = map(int, input().split())
dp = [0] * (R + 1)
ans = 0
for k in range(R, 1, -1):
    tmp = R // k - (L - 1) // k
    dp[k] = tmp * tmp
    j = 2 * k
    while j < R + 1:
        dp[k] -= dp[j]
        j += k
    ans += dp[k]
for g in range(max(2, L), R + 1):
    tmp = R // g - (L - 1) // g
    ans -= 2 * tmp - 1
print(ans)
