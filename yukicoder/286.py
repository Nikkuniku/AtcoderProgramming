n=int(input())
price=[int(input()) for _ in range(n)]

INF = 10**9
dp=[INF]*(1<<n)
dp[0]=0
discount=[0]*(1<<n)
# 定価の合計を記録
for s in range(1<<n):
    x=0
    for j in range(n):
        if (s>>j)&1:
            x+=price[j]
    discount[s]=x
for s in range(1<<n):
    for v in range(n):
        if (s>>v)&1==0:
            x=max(0,price[v]-(discount[s]%1000))
            dp[s|(1<<v)]=min(dp[s]+x,dp[s|(1<<v)])

print(dp[(1<<n)-1])