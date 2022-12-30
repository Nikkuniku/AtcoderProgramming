from sys import stdin
n,m,k=map(int, stdin.readline().split())
mod=998244353
edge=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int, stdin.readline().split())
    u,v=u-1,v-1
    edge[u].append(v)
    edge[v].append(u)

dp=[[0]*n for _ in range(k+1)]
dp[0][0]=1

for i in range(k):
    s=sum(dp[i])
    for j in range(n):
        dp[i+1][j]=(dp[i+1][j]+s-dp[i][j])%mod
        for e in edge[j]:
            dp[i+1][j]-=dp[i][e]
            dp[i+1][j]%=mod

print(dp[k][0]%mod,sep="\n")