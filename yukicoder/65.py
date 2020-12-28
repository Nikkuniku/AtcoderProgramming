k=int(input())

dp=[0]*(k+6+1)
for i in range(k-1,-1,-1):
    dp[i]=1+(dp[i+1]+dp[i+2]+dp[i+3]+dp[i+4]+dp[i+5]+dp[i+6])/6

print(dp[0])