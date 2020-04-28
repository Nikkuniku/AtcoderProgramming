import numpy as np

N=int(input())
H=list(map(int,input().split()))

dp=np.zeros(N+1,dtype=int)

dp[0]=0
dp[1]=0
for i in range(1,N):
    if i==1:
        dp[i+1] = abs(H[1]-H[0])
    else:
        dp[i+1] = min( dp[i] + abs( H[i] - H[i-1] ), dp[i-1] + abs( H[i] - H[i-2] ) )

# print(dp)
print(dp[N])