s=list(input())
t=list(input())

n=len(s)
m=len(t)

dp=[[0]*(m+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else :
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])


from collections import deque
ans=deque([])

while i>0 and j>0:
    if dp[i][j]==dp[i-1][j-1]:
        i-=1
        j-=1
    elif dp[i][j-1]==dp[i][j]:
         j-=1
    elif dp[i-1][j]==dp[i][j]:
        i-=1
    elif dp[i-1][j-1]<dp[i][j]:
        ans.appendleft(s[i-1])
        i-=1
        j-=1


print(''.join(ans))