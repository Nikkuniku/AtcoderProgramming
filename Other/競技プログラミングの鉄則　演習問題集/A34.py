N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (max(A) + 1)
# grundy数の計算
for i in range(max(A) + 1):
    # dp[i-X],dp[i-Y]の値のmexを求める。
    # {0,1,2}からdp[i-X],dp[i-Y]の値を除いて最小値を取れば良い。O(1)
    s = {0, 1, 2}
    if i - X >= 0:
        s.discard(dp[i - X])
    if i - Y >= 0:
        s.discard(dp[i - Y])
    dp[i] = min(s)

xorsum = 0
for a in A:
    xorsum ^= dp[a]
ans = "First" if xorsum else "Second"
print(ans)
