n = int(input())
a = list(map(int, input().split()))
INF = 10**18
# 行動1を行う場合
dp1 = [[INF]*2 for _ in range(n+1)]
dp1[0][1] = a[0]
for i in range(1, n):
    dp1[i][0] = dp1[i-1][1]
    dp1[i][1] = min(dp1[i-1][0], dp1[i-1][1])+a[i]

ans = min(dp1[n-1][0], dp1[n-1][1])
# 行動1を行わない場合
dp2 = [[INF]*2 for _ in range(n+1)]
dp2[0][0] = 0
for i in range(1, n):
    dp2[i][0] = dp2[i-1][1]
    dp2[i][1] = min(dp2[i-1][0], dp2[i-1][1])+a[i]
ans = min(ans, dp2[n-1][1])
print(ans)
