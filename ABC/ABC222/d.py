N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
mod=998244353
dp=[[0]*3001 for _ in range(N+1)]
dp[0]=[1]*3001

for i in range(N):
    a=A[i]
    b=B[i]
    for j in range(a,b+1):
        dp[i+1][j]=dp[i][j]%mod
    if i==N-1:
        break
    # 累積和作成
    for j in range(3000):
        dp[i+1][j+1]+=dp[i+1][j]
        dp[i+1][j+1]%=mod

ans=0
for i in range(a,b+1):
    ans+=dp[N][i]
    ans%=mod
print(ans)