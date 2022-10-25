n = int(input())
a = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(n+1)]
kabu = [[0, 0, 0] for _ in range(n+1)]
for i in range(n):
    # 買う
    dp[i+1][0] = dp[i][0] % a[i]
    kabu[i+1][0] = kabu[i][0] % a[i]
