s=input()
n=len(s)
mod=10**9 + 7

dp=[[0]*(n+1) for _ in range(8)]

status={
0:"c"
,1:"h"
,2:"o"
,3:"k"
,4:"u"
,5:"d"
,6:"a"
,7:"i"
}
for j in range(8):
    for i in range(n):
        if j==0:
            dp[j][i+1] = dp[j][i]
            if s[i]==status[j]:
                dp[j][i+1]+=1
        else:
            dp[j][i+1] = dp[j][i]
            if s[i]==status[j]:
                dp[j][i+1]+=dp[j-1][i]

print(dp[7][n]%mod)