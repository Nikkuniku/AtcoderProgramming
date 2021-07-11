k=int(input())
n=10**5 +1
dp=[0]*(n+1)
dp[0]=1
mod=10**9 + 7
for i in range(1,n):
    if i>=10:
        dp[i]=(dp[i-1]*2-dp[i-10])%mod
    else:
        for j in range(i):
            dp[i]+=dp[j]

if k%9==0:
    ans=dp[k]%mod
else:
    ans=0

print(ans)
