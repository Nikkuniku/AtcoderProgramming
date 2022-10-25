N = int(input())
S = input()
T = [input() for _ in range(N)]
dp = [0]*(len(S)+1)
dp[0] = 1
MOD = 1000000007
for i in range(len(S)+1):
    for t in T:
        if len(S) < i+len(t):
            continue
        if S[i:i+len(t)] == t:
            dp[i+len(t)] += dp[i]
            dp[i+len(t)] %= MOD

print(dp[len(S)])
