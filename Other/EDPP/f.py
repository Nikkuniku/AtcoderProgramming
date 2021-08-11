s=input()
t=input()
n=len(s)
m=len(t)

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[i+1][j+1])
l=dp[n][m]
i=n
j=m
ans=[]
while i>0 and j>0:
    if dp[i][j]==dp[i][j-1]:
       j-=1
    elif dp[i][j]==dp[i-1][j]:
       i-=1
    elif dp[i][j]==dp[i-1][j-1]+1:
        ans.append(i)
        i-=1
        j-=1

lcs=''
ans=sorted(ans)
for p in ans:
    lcs+=s[p-1]
print(lcs)