H, W, K = map(int, input().split())
dp = [[[0]*(1 << (W-1)) for _ in range(W)] for _ in range(H+1)]
dp[0][0][0] = 1
MOD = pow(10, 9) + 7

range_s = []
for s in range(1 << (W-1)):
    flg = True
    for i in range(W-2):
        if (s & (1 << i)) and (s & (1 << (i+1))):
            flg = False
            break
    if flg:
        range_s.append(s)

for h in range(H):
    for w in range(W):
        for s in range_s:
            if w == 0:
                if s & (1 << w):
                    dp[h+1][w][s] += sum(dp[h][w+1])
                else:
                    dp[h+1][w][s] += sum(dp[h][w])
            elif w == W-1:
                if s & (1 << (w-1)):
                    dp[h+1][w][s] += sum(dp[h][w-1])
                else:
                    dp[h+1][w][s] += sum(dp[h][w])
            else:
                if s & (1 << (w-1)) or s & (1 << w):
                    if s & (1 << (w-1)):
                        dp[h+1][w][s] += sum(dp[h][w-1])
                    if s & (1 << w):
                        dp[h+1][w][s] += sum(dp[h][w+1])
                else:
                    dp[h+1][w][s] += sum(dp[h][w])
            dp[h+1][w][s] %= MOD

print(sum(dp[H][K-1]) % MOD)
