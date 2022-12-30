a,b,k=map(int,input().split())
n=61
dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(n):
        dp[i+1][j]+=dp[i][j]
        dp[i][j+1]+=dp[i][j]
def comb(n,r):
    if n>=r:
        return dp[n-r][r]
    else:
        return 0

ans=''
n=a+b
for _ in range(n):
    # aと決めた時
    if a>0:
        if comb(a-1+b,a-1)>=k:
            ans+='a'
            a-=1
        else:
            ans+='b'
            k-=comb(a-1+b,a-1)
            b-=1
    else:
        ans+='b'
        b-=1

print(ans)