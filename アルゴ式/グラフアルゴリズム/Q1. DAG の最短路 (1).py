N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 1 << 30
dp = [INF]*N
dp[0] = 0
for i in range(N-1):
    dp[i+1] = min(dp[i+1], dp[i]+A[i])
    if i-1 >= 0:
        dp[i+1] = min(dp[i+1], dp[i-1]+B[i-1])
print(dp[N-1])
