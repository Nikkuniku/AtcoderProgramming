A,B,C =map(int,input().split())

dp=[[[-1.0]*(101) for _ in range(101)] for _ in range(101) ]
dp[99][99][99]=1.0

def rec(a,b,c):
    # # base case
    if dp[c][a][b]>=0:
        return dp[c][a][b]

    if a==100 or b==100 or c==100:
        return 0

    ans=0
    ans+=a*rec(a+1,b,c)/(a+b+c)
    ans+=b*rec(a,b+1,c)/(a+b+c)
    ans+=c*rec(a,b,c+1)/(a+b+c)
    ans+=1

    dp[c][a][b]=ans

    return ans

print(rec(A,B,C))