n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]

can=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            can[i].append(j)


dp=[[0]*(1<<n) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    c=can[i]
    for s in range(1<<n):
        for v in range(n):
            if (s>>v)&1==0:
                dp[i+1][s|(1<<v)]+=dp[i][s]

print(dp[0][0],sep="\n")