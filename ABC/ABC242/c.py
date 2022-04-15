n=int(input())
mod=998244353
dp=[[0]*9 for _ in range(n)]
dp[0]=[1]*9

for i in range(n-1):
    for j in range(9):
        for k in [-1,0,1]:
            if 0<=j+k<=8:
                dp[i+1][j]+=dp[i][j+k]
                dp[i+1][j]%=mod

ans=sum(dp[n-1])%mod
print(ans)