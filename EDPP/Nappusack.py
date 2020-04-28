import numpy as np

N,W = map(int,input().split())

#dp配列作成
dp=[[0]*(W+1)]*(N+1)

for i in range(N):
    v_i,w_i =map(int,input().split())
    for w in range(W+1):
        if w >= w_i:
            dp[i+1][w] = max( dp[i][w-w_i]+v_i, dp[i][w] )
        else:
            dp[i+1][w] = dp[i][w]
    
    print(dp,sep="\n")

print(dp[N][W])
