n=int(input())
s=input()
mod=10**9 + 7

dp=[[0]*(n+1) for _ in range(7)]

status={
0:"a"
,1:"t"
,2:"c"
,3:"o"
,4:"d"
,5:"e"
,6:"r"
}
for j in range(7):
    for i in range(n):
        if j==0:
            dp[j][i+1] = dp[j][i]
            if s[i]==status[j]:
                dp[j][i+1]+=1
        else:
            dp[j][i+1] = dp[j][i]
            if s[i]==status[j]:
                dp[j][i+1]+=dp[j-1][i]

print(dp[6][n]%mod)